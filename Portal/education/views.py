from rest_framework import viewsets
from .models import Institution
from .models import Certification
from . import serializers


class InstitutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = serializers.InstitutionSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CertificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = serializers.CertificationSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)