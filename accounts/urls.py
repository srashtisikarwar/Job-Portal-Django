
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.RegisterUser, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('employer/dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('employer/profile/', views.manage_profile, name='manage_profile'),
    path('candidate/dashboard/', views.candidate_dashboard, name='candidate_dashboard'),
    path('candidate/profile/edit',views.edit_candidate_profile, name='edit_candidate_profile'),
    path('candidate/my_applications/',views.my_applications, name='my_applications'),
    path('update/application_status/<int:application_id>/', views.update_application_status, name='update_application_status'),
    path('set-theme/', views.set_theme, name='set_theme'),
]