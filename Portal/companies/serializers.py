from rest_framework import serializers
from .models import Company
from .models import Organization


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        partial = True
        fields = ['id', 'owner', 'name', 'url', 'location', 'coordinates', 'summary', 'size', 'employees', 'contact_name',
                  'contact_email', 'contact_phone', 'contact_position']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        partial = True
        fields = ['name', 'url', 'location', 'coordinates', 'summary', 'size', 'employees']
