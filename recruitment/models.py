from django.db import models

class Application(models.Model):
    # Section 1: Basic Details
    POST_CHOICES = [
        ('Assistant Professor', 'Assistant Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Professor', 'Professor'),
    ]
    CATEGORY_CHOICES = [
        ('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), 
        ('ST', 'ST'), ('EWS', 'EWS'), ('PwD', 'PwD')
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')
    ]

    post_applied_for = models.CharField(max_length=50, choices=POST_CHOICES)
    department = models.JSONField() # Checkboxes
    full_name = models.CharField(max_length=200)
    father_mother_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    nationality = models.CharField(max_length=50)
    dob = models.DateField()
    marital_status = models.CharField(max_length=50)
    aadhaar_number = models.CharField(max_length=12)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=10)
    correspondence_address = models.TextField()
    photograph = models.FileField(upload_to='photographs/', null=True, blank=True)

    # Section 2: Education
    class10_board = models.CharField(max_length=100)
    class10_school = models.CharField(max_length=200)
    class10_year = models.IntegerField()
    class10_percentage = models.FloatField()

    class12_board = models.CharField(max_length=100)
    class12_school = models.CharField(max_length=200)
    class12_year = models.IntegerField()
    class12_percentage = models.FloatField()

    diploma_board = models.CharField(max_length=100, blank=True, null=True)
    diploma_college = models.CharField(max_length=200, blank=True, null=True)
    diploma_year = models.IntegerField(blank=True, null=True)
    diploma_percentage = models.FloatField(blank=True, null=True)

    ug_degree = models.CharField(max_length=100)
    ug_branch = models.CharField(max_length=100)
    ug_university = models.CharField(max_length=200)
    ug_institution = models.CharField(max_length=200)
    ug_mode = models.CharField(max_length=50)
    ug_year = models.IntegerField()
    ug_percentage = models.FloatField()

    pg_degree = models.CharField(max_length=100)
    pg_branch = models.CharField(max_length=100)
    pg_university = models.CharField(max_length=200)
    pg_institution = models.CharField(max_length=200)
    pg_mode = models.CharField(max_length=50)
    pg_year = models.IntegerField()
    pg_percentage = models.FloatField()

    has_phd = models.BooleanField(default=False)
    phd_university = models.CharField(max_length=200, blank=True, null=True)
    phd_institution = models.CharField(max_length=200, blank=True, null=True)
    phd_mode = models.CharField(max_length=50, blank=True, null=True)
    phd_year = models.IntegerField(blank=True, null=True)
    phd_specialization = models.CharField(max_length=200, blank=True, null=True)
    phd_title = models.CharField(max_length=500, blank=True, null=True)

    # Section 3: Additional Qual
    net_qualified = models.BooleanField(default=False)
    net_year = models.IntegerField(blank=True, null=True)
    net_subject = models.CharField(max_length=100, blank=True, null=True)

    gate_qualified = models.BooleanField(default=False)
    gate_year = models.IntegerField(blank=True, null=True)
    gate_rank = models.IntegerField(blank=True, null=True)

    other_certifications = models.JSONField(default=list, blank=True)

    # Section 4: Experience
    teaching_exp_years = models.FloatField()
    industry_exp_years = models.FloatField(default=0)
    research_exp_years = models.FloatField(default=0)
    total_experience = models.FloatField(default=0, editable=False) # Auto-calculated

    def save(self, *args, **kwargs):
        self.total_experience = (self.teaching_exp_years or 0) + (self.industry_exp_years or 0) + (self.research_exp_years or 0)
        super().save(*args, **kwargs)

    curr_organization = models.CharField(max_length=200, blank=True, null=True)
    curr_designation = models.CharField(max_length=100, blank=True, null=True)
    curr_nature = models.CharField(max_length=50, blank=True, null=True)
    curr_duration_from = models.DateField(blank=True, null=True)
    curr_duration_to = models.DateField(blank=True, null=True)
    curr_pay_scale = models.CharField(max_length=100, blank=True, null=True)
    curr_salary = models.CharField(max_length=100, blank=True, null=True)

    previous_employment = models.JSONField(default=list, blank=True)

    # Section 5: Research & Academic
    pub_sci = models.IntegerField(default=0)
    pub_esci = models.IntegerField(default=0)
    pub_ugc = models.IntegerField(default=0)
    pub_others = models.IntegerField(default=0)
    publication_list_pdf = models.FileField(upload_to='publications/', null=True, blank=True)

    google_scholar_link = models.URLField(blank=True, null=True)
    h_index = models.IntegerField(default=0)
    i10_index = models.IntegerField(default=0)

    # Split patents into Utility and Design based on PDF notes
    utility_patents_filed = models.IntegerField(default=0)
    utility_patents_published = models.IntegerField(default=0)
    utility_patents_granted = models.IntegerField(default=0)
    
    design_patents_filed = models.IntegerField(default=0)
    design_patents_published = models.IntegerField(default=0)
    design_patents_granted = models.IntegerField(default=0)

    sponsored_projects = models.JSONField(default=list, blank=True)
    consultancy_work = models.JSONField(default=list, blank=True)

    phd_guidance_completed = models.IntegerField(default=0)
    phd_guidance_ongoing = models.IntegerField(default=0)

    # Section 6: Teaching
    teaching_subjects = models.JSONField(default=list, blank=True)
    ug_pg_level = models.JSONField(default=list, blank=True) # New field for checkboxes (UG, PG)

    # Section 7: FDP
    fdp_attended = models.IntegerField(default=0)
    fdp_organized = models.IntegerField(default=0)

    # Section 8: Admin & Prof
    administrative_roles = models.JSONField(default=list, blank=True)
    professional_memberships = models.JSONField(default=list, blank=True)
    awards_recognitions = models.JSONField(default=list, blank=True)

    # Section 9: Statements
    area_of_specialization = models.CharField(max_length=300)
    teaching_statement = models.TextField()
    research_statement = models.TextField()

    # Section 10: Institutional Suitability
    why_akgec = models.TextField(help_text="Reason for choosing AKGEC")
    suitability_statement = models.TextField(help_text="Statement on how you are best suited for the post")

    # Section 11: Documents (Basic single fields)
    cv_pdf = models.FileField(upload_to='cv/')
    # The following are kept for backward compatibility but multiple uploads will use ApplicationDocument
    degree_certificates = models.FileField(upload_to='certificates/', blank=True, null=True)
    experience_certificates = models.FileField(upload_to='experience/', blank=True, null=True)
    awards_documents = models.FileField(upload_to='awards/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.post_applied_for}"

class ApplicationDocument(models.Model):
    DOCUMENT_TYPES = [
        ('degree', 'Degree Certificate'),
        ('experience', 'Experience Certificate'),
        ('award', 'Award / Recognition'),
        ('other', 'Other'),
    ]
    application = models.ForeignKey(Application, related_name='additional_documents', on_delete=models.CASCADE)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to='additional_docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.application.full_name} - {self.document_type}"
