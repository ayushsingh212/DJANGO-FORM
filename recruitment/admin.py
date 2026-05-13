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
    
    fieldsets = (
        ('Basic Details', {
            'fields': ('post_applied_for', 'department', 'full_name', 'father_mother_name', 'gender', 'category', 'nationality', 'dob', 'marital_status', 'aadhaar_number', 'email', 'mobile_number', 'correspondence_address', 'photograph')
        }),
        ('Education', {
            'fields': (
                'class10_board', 'class10_school', 'class10_year', 'class10_percentage',
                'class12_board', 'class12_school', 'class12_year', 'class12_percentage',
                'diploma_board', 'diploma_college', 'diploma_year', 'diploma_percentage',
                'ug_degree', 'ug_branch', 'ug_university', 'ug_institution', 'ug_mode', 'ug_year', 'ug_percentage',
                'pg_degree', 'pg_branch', 'pg_university', 'pg_institution', 'pg_mode', 'pg_year', 'pg_percentage',
                'has_phd', 'phd_university', 'phd_institution', 'phd_mode', 'phd_year', 'phd_specialization', 'phd_title'
            )
        }),
        ('Additional Qualifications', {
            'fields': ('net_qualified', 'net_year', 'net_subject', 'gate_qualified', 'gate_year', 'gate_rank', 'other_certifications')
        }),
        ('Experience', {
            'fields': ('teaching_exp_years', 'industry_exp_years', 'research_exp_years', 'total_experience', 'curr_organization', 'curr_designation', 'curr_nature', 'curr_duration_from', 'curr_duration_to', 'curr_pay_scale', 'curr_salary', 'previous_employment')
        }),
        ('Research & Academic', {
            'fields': ('pub_sci', 'pub_esci', 'pub_ugc', 'pub_others', 'publication_list_pdf', 'google_scholar_link', 'h_index', 'i10_index', 'utility_patents_filed', 'utility_patents_published', 'utility_patents_granted', 'design_patents_filed', 'design_patents_published', 'design_patents_granted', 'sponsored_projects', 'consultancy_work', 'phd_guidance_completed', 'phd_guidance_ongoing')
        }),
        ('Teaching & FDP', {
            'fields': ('teaching_subjects', 'ug_pg_level', 'fdp_attended', 'fdp_organized')
        }),
        ('Admin & Professional', {
            'fields': ('administrative_roles', 'professional_memberships', 'awards_recognitions')
        }),
        ('Statements', {
            'fields': ('area_of_specialization', 'teaching_statement', 'research_statement')
        }),
        ('Institutional Suitability', {
            'fields': ('why_akgec', 'suitability_statement')
        }),
        ('Documents', {
            'fields': ('cv_pdf', 'degree_certificates', 'experience_certificates', 'awards_documents')
        }),
    )
    readonly_fields = ('total_experience', 'created_at')

    def display_total_experience(self, obj):
        return obj.total_experience
    display_total_experience.short_description = 'Total Exp (Years)'

@admin.register(ApplicationDocument)
class ApplicationDocumentAdmin(admin.ModelAdmin):
    list_display = ('application', 'document_type', 'file', 'uploaded_at')
