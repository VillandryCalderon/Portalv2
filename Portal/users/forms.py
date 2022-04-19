from django import forms
from users.models import UserProfile,UserEducation
from django.contrib.auth.models import User,Group

from companies.models import Organization
from education.models import Certification
from education.models import Institution
from . import constants


class FormularioUser(forms.ModelForm):
    

    class Meta:
        model= UserProfile
        fields=('first_name','last_name','birthday','phone','location','coordinates','salary_min','job_type','type_of_contract','Createresumen')
        widgets={ 'birthday': forms.DateInput(attrs={'type':'date'}),
                 'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su nombre'}),
                 'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese sus apellidos'}),
                 'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'+506 8888 8888'}),
                 'location': forms.TextInput(attrs={'class':'form-control'}),
                 'coordinates': forms.TextInput(attrs={'class':'form-control','placeholder':'Distrito'}),
                 
                 }
      
class FormularioEducation(forms.ModelForm):
        
    class Meta:
        model = UserEducation
        fields=('institution','title','start_date','end_date','in_progress')
        
  


        
        
        

        
        
        