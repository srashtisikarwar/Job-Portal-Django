from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    role=models.CharField(max_length=50,choices=[('admin','Admin'),('employer','Employer'),('candidate','Candidate')])
    def __str__(self):
        return self.username and self.role

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_website = models.URLField()
    company_location = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)

def __str__(self):
    return self.user.username

@property
def resume(self):
        """Return candidate's resume from profile"""
        if hasattr(self.candidate, 'candidateprofile') and self.candidate.candidateprofile.resume:
            return self.candidate.candidateprofile.resume.url
        return None