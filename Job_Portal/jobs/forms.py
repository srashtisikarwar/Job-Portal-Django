from .models import Job
from django import forms
from .models import User

class jobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary']


