from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Application, ApplicationDocument
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        # Extract additional documents before standard creation
        # We expect files in request.FILES with keys matching document types
        # OR a generic 'additional_docs' key with multiple files.
        # Based on PDF "Allow multiple uploads", we'll handle them.
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.save()

        # Handle multiple file uploads for different types
        doc_types = ['degree', 'experience', 'award', 'other']
        for doc_type in doc_types:
            files = request.FILES.getlist(f'{doc_type}_files')
            for f in files:
                ApplicationDocument.objects.create(
                    application=application,
                    document_type=doc_type,
                    file=f
                )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

