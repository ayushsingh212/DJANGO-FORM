from rest_framework import serializers
from .models import Application, ApplicationDocument

class ApplicationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDocument
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    additional_documents = ApplicationDocumentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Application
        fields = '__all__'
