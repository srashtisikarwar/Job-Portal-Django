from django.db import models
from accounts.models import User



# Create your models here.
from django.db import models
from django.conf import settings

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
        ('Remote', 'Remote'),
    ]

    EXPERIENCE_CHOICES = [
        ('Fresher', 'Fresher'),
        ('1-3 Years', '1-3 Years'),
        ('3-5 Years', '3-5 Years'),
        ('5+ Years', '5+ Years'),
    ]

    employer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField(blank=True)

    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Enter salary in INR per month"
    )

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES,
        default='Full-Time'
    )

    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default='Fresher'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    candidate = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'candidate'}
    )

    resume = models.FileField(
        upload_to='resumes/',
        blank=False,
        null=False
    )

    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    
    # Add this new field
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    class Meta:
        unique_together = ('job', 'candidate')

    def __str__(self):
        return f"{self.candidate.username} - {self.job.title} ({self.status})"