from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        # We can handle custom logic here if needed
        return super().create(request, *args, **kwargs)
