from django import forms
from infoprofile.models import UserProfile
from django.contrib.auth.models import User,Group

from companies.models import Organization
from education.models import Certification
from education.models import Institution
from . import constants


class FormularioUser(forms.ModelForm):
    

    class Meta:
        model= UserProfile
        fields=('first_name','last_name','birthday','phone','location','coordinates','salary_min','job_type','type_of_contract','Createresumen')
        widgets={'birthday': forms.DateInput(attrs={'type':'date'})}
        
        
        
  
