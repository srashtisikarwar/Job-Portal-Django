from decimal import Decimal, InvalidOperation

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Job, JobApplication, User
from .forms import jobForm
from django.http import HttpResponseForbidden
from django.db.models import Q

def home(request):
    jobs_count = Job.objects.count()
    context = {
        'jobs_count': jobs_count,
    }
    return render(request, 'home.html', context)

# List all jobs




def job_list(request):
    query = request.GET.get("q", "").strip()
    location = request.GET.get("location", "").strip()

    jobs = Job.objects.all()
    exact_match = False

    # CASE 1: Job title + location both given
    if query and location:
        exact_jobs = jobs.filter(
            title__iexact=query,
            location__iexact=location
        )

        if exact_jobs.exists():
            jobs = exact_jobs
            exact_match = True
        else:
            jobs = jobs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(location__icontains=location)
            )

    # CASE 2: Only job title / keyword
    elif query:
        exact_jobs = jobs.filter(title__iexact=query)

        if exact_jobs.exists():
            jobs = exact_jobs
            exact_match = True
        else:
            jobs = jobs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )

    # CASE 3: Only location
    elif location:
        jobs = jobs.filter(location__icontains=location)

    context = {
        "jobs": jobs,
        "query": query,
        "location": location,
        "exact_match": exact_match,
    }

    return render(request, "jobs/job_list.html", context)


@login_required(login_url='login')
def add_job(request):

    if request.user.role != 'employer':
        return HttpResponseForbidden("You are not allowed to post jobs")

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        requirements = request.POST.get('requirements') 
        location = request.POST.get('location')
        job_type = request.POST.get('job_type')
        experience_level = request.POST.get('experience_level')
        salary_input = request.POST.get('salary')

        if not all([title, description, location, job_type, experience_level]):
            messages.error(request, "Please fill all required fields")
            return render(request, 'jobs/add_job.html')

        salary = None
        if salary_input:
            try:
                salary = Decimal(salary_input)
            except InvalidOperation:
                messages.error(request, "Invalid salary")
                return render(request, 'jobs/add_job.html')

        Job.objects.create(
            employer=request.user,
            title=title,
            description=description,
            requirements=requirements,
            location=location,
            job_type=job_type,
            experience_level=experience_level,
            salary=salary
        )

        messages.success(request, "Job posted successfully!")
        return redirect('employer_dashboard')

    return render(request, 'jobs/add_job.html')

@login_required(login_url='login')
def edit_job(request, job_id):
    job_instance = get_object_or_404(Job, id=job_id)

    # Ensure only the employer who posted the job can edit it
    if job_instance.employer != request.user:
        return HttpResponseForbidden("You are not allowed to edit this job")

    if request.method == 'POST':
        form = jobForm(request.POST, instance=job_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Job updated successfully!")
            return redirect('employer_dashboard')
    else:
        form = jobForm(instance=job_instance)

    return render(request, 'jobs/edit_job.html', {'form': form, 'job': job_instance})
@login_required(login_url='login')
def delete_job(request, job_id):
    job_instance = get_object_or_404(Job, id=job_id)

    # Ensure only the employer who posted the job can delete it
    if job_instance.employer != request.user:
        return HttpResponseForbidden("You are not allowed to delete this job")

    if request.method == 'POST':
        job_instance.delete()
        messages.success(request, "Job deleted successfully!")
        return redirect('employer_dashboard')

    return render(request, 'jobs/delete_job.html', {'job': job_instance})


# Apply for a job (candidates only)
@login_required(login_url='login')
def apply_job(request, job_id):
    # Only candidates can apply
    if not hasattr(request.user, 'role') or request.user.role != 'candidate':
        return HttpResponseForbidden("You are not allowed to apply for jobs")

    job_instance = get_object_or_404(Job, id=job_id)

    # Prevent duplicate application
    if JobApplication.objects.filter(job=job_instance, candidate=request.user).exists():
        messages.success(request, "You have already applied for this job.")
        return redirect('job_detail', job_id=job_instance.id)

    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')   # ✅ resume file

        if not resume:
            messages.error(request, "Please upload your resume.")
            return redirect('apply_job', job_id=job_instance.id)

        JobApplication.objects.create(
            job=job_instance,
            candidate=request.user,
            cover_letter=cover_letter,
            resume=resume        # ✅ save resume
        )

        messages.success(request, "Application submitted successfully!")
        return redirect('job_list')

    return render(request, 'jobs/apply_job.html', {'job': job_instance})

# Job detail page
def job_detail(request, job_id):
    job_instance = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job_instance})


# Redirect to job list
@login_required(login_url='register')
def jobs_redirect(request):
    return redirect('job_list')


# ...existing code...

def splash(request):
    """Display splash screen with logo"""
    return render(request, 'Splash.html')

# ...existing code...
