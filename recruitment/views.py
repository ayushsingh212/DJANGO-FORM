from django.db import transaction
from django.shortcuts import render, get_object_or_404
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


def application_list_view(request):
    applications = Application.objects.all().order_by('-created_at')
    return render(request, 'recruitment/list.html', {'applications': applications})


def application_detail_view(request, pk):
    application = get_object_or_404(Application, pk=pk)
    # Fetch additional documents grouped by type or just all
    docs = application.additional_documents.all()
    return render(request, 'recruitment/detail.html', {'application': application, 'docs': docs})


