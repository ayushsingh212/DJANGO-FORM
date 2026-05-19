import re
from rest_framework import serializers
from .models import Application, ApplicationDocument
from django.utils import timezone

class ApplicationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDocument
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    additional_documents = ApplicationDocumentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Application
        fields = '__all__'

    def validate_mobile_number(self, value):
        if not re.match(r'^\d{10}$', value):
            raise serializers.ValidationError("Mobile number must be exactly 10 digits.")
        return value

    def validate_aadhaar_number(self, value):
        if not re.match(r'^\d{12}$', value):
            raise serializers.ValidationError("Aadhaar number must be exactly 12 digits.")
        return value

    def validate_dob(self, value):
        if value >= timezone.now().date():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value

    def _validate_percentage(self, value, field_name):
        if value < 0 or value > 100:
            raise serializers.ValidationError(f"{field_name} must be between 0 and 100.")
        return value

    def validate_class10_percentage(self, value):
        return self._validate_percentage(value, "Class 10 percentage")

    def validate_class12_percentage(self, value):
        return self._validate_percentage(value, "Class 12 percentage")

    def validate_ug_percentage(self, value):
        return self._validate_percentage(value, "UG percentage")

    def validate_pg_percentage(self, value):
        return self._validate_percentage(value, "PG percentage")

    def validate_diploma_percentage(self, value):
        if value is not None:
            return self._validate_percentage(value, "Diploma percentage")
        return value

    def validate_email(self, value):
        return value.lower() # Ensure email is lowercase for consistency

    def _validate_year(self, value, field_name):
        current_year = timezone.now().year
        if value < 1900 or value > current_year + 1: # Allow +1 for future graduates
            raise serializers.ValidationError(f"{field_name} is invalid.")
        return value

    def validate_class10_year(self, value):
        return self._validate_year(value, "Class 10 passing year")

    def validate_class12_year(self, value):
        return self._validate_year(value, "Class 12 passing year")

    def validate_ug_year(self, value):
        return self._validate_year(value, "UG passing year")

    def validate_pg_year(self, value):
        return self._validate_year(value, "PG passing year")

    def validate_phd_year(self, value):
        if value:
            return self._validate_year(value, "PhD passing year")
        return value

    def validate_department(self, value):
        if not isinstance(value, list) or len(value) == 0:
            raise serializers.ValidationError("At least one department must be selected.")
        return value

    def validate(self, data):
        # Cross-field validation (handles partial updates by referencing existing instance)
        instance = self.instance

        has_phd = data.get('has_phd', getattr(instance, 'has_phd', False) if instance else False)
        if has_phd:
            required_phd_fields = ['phd_university', 'phd_year', 'phd_specialization', 'phd_title']
            for field in required_phd_fields:
                val = data.get(field, getattr(instance, field, None) if instance else None)
                if not val:
                    raise serializers.ValidationError({field: "This field is required if you have a PhD."})
        
        net_qualified = data.get('net_qualified', getattr(instance, 'net_qualified', False) if instance else False)
        net_year = data.get('net_year', getattr(instance, 'net_year', None) if instance else None)
        if net_qualified and not net_year:
            raise serializers.ValidationError({'net_year': "NET year is required if NET qualified."})
            
        gate_qualified = data.get('gate_qualified', getattr(instance, 'gate_qualified', False) if instance else False)
        gate_year = data.get('gate_year', getattr(instance, 'gate_year', None) if instance else None)
        if gate_qualified and not gate_year:
            raise serializers.ValidationError({'gate_year': "GATE year is required if GATE qualified."})

        return data

