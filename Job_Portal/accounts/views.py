from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods
import json

from .forms import RegistrationForm, EmployerProfileForm
from .models import User, EmployerProfile, CandidateProfile
from jobs.models import Job, JobApplication




def RegisterUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                f"Account created successfully, {user.username}!"
            )

            if user.role == 'candidate':
                CandidateProfile.objects.get_or_create(user=user)
                return redirect('candidate_dashboard')

            if user.role == 'employer':
                EmployerProfile.objects.get_or_create(user=user)
                return redirect('employer_dashboard')

            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect(
            'employer_dashboard'
            if request.user.role == 'employer'
            else 'candidate_dashboard'
        )

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            login(request, form.get_user())
            return redirect(
                'employer_dashboard'
                if request.user.role == 'employer'
                else 'candidate_dashboard'
            )
        else:
            messages.error(
                request,
                'Invalid username or password. Please register yourself if you are new user.'
            )

    return render(request, 'accounts/login.html', {'form': form})


@login_required(login_url='login')
def employer_dashboard(request):
    if request.user.role != 'employer':
        return HttpResponseForbidden("Access denied")

    profile, _ = EmployerProfile.objects.get_or_create(
        user=request.user
    )

    jobs = Job.objects.filter(employer=request.user)

    job_applications = {
        job.id: JobApplication.objects.filter(job=job)
        for job in jobs
    }

    return render(request, 'accounts/employer_dashboard.html', {
        'profile': profile,
        'jobs': jobs,
        'job_applications': job_applications
    })

@login_required(login_url='login')
def manage_profile(request):
    if request.user.role != 'employer':
        return HttpResponseForbidden("Access denied")

    profile, _ = EmployerProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        form = EmployerProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('employer_dashboard')
    else:
        form = EmployerProfileForm(instance=profile)

    return render(request, 'accounts/employerprofile.html', {
        'form': form,
        'profile': profile
    })


@login_required(login_url='login')
def candidate_dashboard(request):
    if request.user.role != 'candidate':
        return HttpResponseForbidden("Access denied")

    applications_count = JobApplication.objects.filter(
        candidate=request.user
    ).count()

    return render(request, 'accounts/candidate_dashboard.html', {
        'applications_count': applications_count
    })

@login_required(login_url='login')
def my_applications(request):
    if request.user.role != 'candidate':
        return HttpResponseForbidden("Access denied")

    applications = JobApplication.objects.filter(
        candidate=request.user
    )

    return render(request, 'accounts/my_application.html', {
        'applications': applications
    })

@login_required(login_url='login')
def edit_candidate_profile(request):
    if request.user.role != 'candidate':
        return HttpResponseForbidden("Access denied")

    profile, _ = CandidateProfile.objects.get_or_create(
        user=request.user
    )
    

    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.save()

        profile.skills = request.POST.get('skills')
        profile.experience = request.POST.get('experience')

        if request.FILES.get('resume'):
            profile.resume = request.FILES.get('resume')

        profile.save()

        messages.success(request, "Profile updated successfully")
        return redirect('candidate_dashboard')

    return render(request, 'accounts/edit_candidate_profile.html', {
        'profile': profile
    })
@login_required(login_url='login')
def update_application_status(request, application_id):
    if request.user.role != 'employer':
        return HttpResponseForbidden("Access denied")

    try:
        application = JobApplication.objects.get(id=application_id)
    except JobApplication.DoesNotExist:
        messages.error(request, "Application not found.")
        return redirect('employer_dashboard')

    if application.job.employer != request.user:
        return HttpResponseForbidden("You are not authorized to update this application.")

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(JobApplication.STATUS_CHOICES).keys():
            application.status = new_status
            application.save()
            messages.success(request, "Application status updated successfully.")
        else:
            messages.error(request, "Invalid status selected.")

    return redirect('employer_dashboard')


@require_http_methods(["POST"])
def set_theme(request):
    """Set theme preference in session."""
    try:
        data = json.loads(request.body)
        theme = data.get('theme', 'light')
        if theme in ['light', 'dark']:
            request.session['theme'] = theme
            return JsonResponse({'status': 'success', 'theme': theme})
    except:
        pass
    return JsonResponse({'status': 'error'}, status=400)
    return redirect('employer_dashboard')
    