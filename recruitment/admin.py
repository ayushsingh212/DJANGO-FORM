from django.contrib import admin
from .models import Application, ApplicationDocument

class ApplicationDocumentInline(admin.TabularInline):
    model = ApplicationDocument
    extra = 1

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'post_applied_for', 'email', 'mobile_number', 'display_total_experience', 'created_at')
    search_fields = ('full_name', 'email', 'mobile_number')
    list_filter = ('post_applied_for', 'category', 'gender', 'created_at')
    inlines = [ApplicationDocumentInline]

    def display_total_experience(self, obj):
        return obj.total_experience
    display_total_experience.short_description = 'Total Exp (Years)'

@admin.register(ApplicationDocument)
class ApplicationDocumentAdmin(admin.ModelAdmin):
    list_display = ('application', 'document_type', 'file', 'uploaded_at')
