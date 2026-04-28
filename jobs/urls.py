from django.urls import path
from .views import add_job,apply_job, delete_job, job_detail, job_list, jobs_redirect, edit_job


urlpatterns = [
    path('', job_list, name='job_list'),
    path('jobs/', jobs_redirect, name='jobs_redirect'),
    path('jobs/list/', job_list, name='job_list'),
    path('jobs/<int:job_id>/', job_detail, name='job_detail'),
    path('jobs/add/', add_job, name='add_job'),
    path('jobs/apply/<int:job_id>/', apply_job, name='apply_job'),
    path('jobs/edit/<int:job_id>/', edit_job, name='edit_job'),
    path('jobs/delete/<int:job_id>/', delete_job, name='delete_job'),
]