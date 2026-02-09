from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CandidateProfile, EmployerProfile, User

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role',)

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Information', {'fields': ('role',)}),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Role Information', {'fields': ('role',)}),
    )

admin.site.register(User, UserAdmin)
admin.site.site_header = "Job Portal Administration"
admin.site.site_title = "Job Portal Admin"
admin.site.index_title = "Welcome to Job Portal Admin Panel"
admin.site.register(EmployerProfile)
admin.site.register(CandidateProfile)