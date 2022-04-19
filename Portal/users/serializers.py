from rest_framework import serializers
from .models import UserProfile
from .models import UserEducation


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['pk', 'user', 'first_name', 'last_name', 'birthday', 'email', 'phone', 'location', 'coordinates',
                  'salary_min', 'job_type', 'type_of_contract','Createresumen']
        
    def to_representation(self,instance):
        return {
            'pk': instance.pk,
            'user':instance.user,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'birthday': instance.birthday,
            'email': instance.email, 
            'phone': instance.phone, 
            'location': instance.location,
            'coordinates': instance.coordinates,
            'salary_min': instance.salary_min,
            'job_type': instance.job_type,
            'type_of_contract': instance.type_of_contract,
            'Createresumen': instance.file.url,
        } 



class UserEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEducation
        fields = ['userprofile', 'institution', 'title', 'start_date', 'end_date', 'in_progress', 'description']
