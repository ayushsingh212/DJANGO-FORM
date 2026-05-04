from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'post_applied_for', 'email', 'mobile_number', 'created_at')
    search_fields = ('full_name', 'email', 'mobile_number')
    list_filter = ('post_applied_for', 'category', 'gender', 'created_at')
