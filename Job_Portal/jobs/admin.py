from django.contrib import admin
from django.utils.html import format_html
from .models import Job,JobApplication

# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'get_company_name',
        'location',
        'job_type',
        'experience_level',
        'created_at',
    )

    list_filter = ('job_type', 'experience_level', 'created_at')
    search_fields = ('title', 'employer__username')

    def get_company_name(self, obj):
        if hasattr(obj.employer, 'employerprofile'):
            return obj.employer.employerprofile.company_name
        return "No Profile"

    get_company_name.short_description = 'Company'
# Inline applications inside Job
class JobApplicationInline(admin.TabularInline):
    model = JobApplication
    extra = 0
    readonly_fields = ('candidate', 'resume_link', 'cover_letter', 'applied_at')

    def resume_link(self, obj):
        if obj.resume:
            return format_html(
                '<a href="{}" target="_blank">Download Resume</a>',
                obj.resume.url
            )
        return "No Resume"

    resume_link.short_description = "Resume"

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):   # ✅ IMPORTANT
    list_display = (
        'job',
        'candidate',
        'resume_link',
        'applied_at'
    )
    list_filter = ('applied_at',)
    search_fields = ('job__title', 'candidate__username')
    readonly_fields = ('resume_link',)

    def resume_link(self, obj):
        if obj.resume:
            return format_html(
                '<a href="{}" target="_blank">Download Resume</a>',
                obj.resume.url
            )
        return "No Resume"

    resume_link.short_description = "Resume"