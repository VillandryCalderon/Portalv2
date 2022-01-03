from rest_framework import serializers
from .models import UserProfile
from .models import UserEducation


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['pk', 'user', 'first_name', 'last_name', 'birthday', 'email', 'phone', 'location', 'coordinates',
                  'salary_min', 'job_type', 'type_of_contract']



class UserEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEducation
        fields = ['userprofile', 'institution', 'title', 'start_date', 'end_date', 'in_progress', 'description']
