from venv import create
from django.db import models
from automatic_crud.models import BaseModel
from django.contrib.auth.models import User
from education.models import Certification
from education.models import Institution
from companies.models import Organization
from . import constants
# Create your models here.


class UserProfile(BaseModel):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     first_name = models.CharField(max_length=64)
     last_name = models.CharField(max_length=64)
     birthday = models.DateField(verbose_name='Fecha Nacimiento')    
     email = models.EmailField()
     phone = models.CharField(verbose_name='Telefono', max_length=16, blank=True)
     location = models.CharField(max_length=120, blank=True)
     coordinates = models.CharField(max_length=64, help_text='Distrito,cantón', blank=True)
    
     salary_min = models.IntegerField('Salario Minimo', help_text=('₡'), blank=True, null=True)
     job_type = models.CharField('Preferencia de empleo', max_length=32, choices=constants.JOB_TYPE,blank=True)
     type_of_contract = models.CharField('Tipo de Contrato', max_length=32,choices=constants.TYPE_OF_CONTRACT, blank=True)
     Createresumen=models.FileField(upload_to='Resumenpostulantes',verbose_name="Cargar Curriculum",blank=True,null=True)
     
     login_required = True
     permission_required = ()
     model_permissions = True
     
    
     class Meta:
            verbose_name = ('User_Profile')
            verbose_name_plural = ('User_Profile')
            
            def __all__(self):
         
             return self.user.__all__ 

class UserEducation(BaseModel):
    userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name='user_Education')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    title = models.CharField(('Grado'), max_length=64)
    start_date = models.DateField(auto_now_add=True,verbose_name='Fecha Inicio')
    end_date = models.DateField(auto_now_add=True,verbose_name='Fecha Finalizacion', blank=True, null=True)
    in_progress = models.BooleanField(default=False,verbose_name='En Progreso')
    description = models.TextField()
    
    
    exclude_fields = ['start_date','end_date','description','model_state']

    class Meta:
        verbose_name = ('Education')
        verbose_name_plural = ('Education')
        ordering =  ('-start_date', '-end_date')

    def __str__(self):
        return self.title
 
 
class UserCertification(BaseModel):
        userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
        name = models.CharField('Certificado', max_length=64)
        start_date = models.DateField(auto_now_add=True, verbose_name='Fecha Inicio')
        end_date = models.DateField(auto_now_add=True,verbose_name='Fecha Finalizacion', blank=True, null=True)
        in_progress = models.BooleanField(default=False,verbose_name='En Progreso')

        class Meta:
         verbose_name = ('Certificaciónes')
         verbose_name_plural = ('Certificaciónes')
         ordering = ('-start_date', '-end_date')

        def __str__(self):
            return self.name
        



class UserJob(BaseModel):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(('Titulo'), max_length=64)
    start_date = models.DateField(('Fecha Inicio'))
    end_date = models.DateField(('Fecha Finalizacion'), blank=True, null=True)
    in_progress = models.BooleanField(default=False,verbose_name=('En Progreso'))

    class Meta:
        verbose_name = ('Trabajo')
        verbose_name_plural = ('Trabajos')
        ordering = ('start_date', 'end_date')

    def __str__(self):
        return self.title


class UserURL(BaseModel):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    network = models.CharField(max_length=32, choices=constants.USER_LINKS)
    url = models.CharField(max_length=64)

    class Meta:
        verbose_name = ('User Url')
        verbose_name_plural = ('User Urls')

    def __str__(self):
        return '{}: {}'.format(self.network, self.url)



class UserProject(BaseModel):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=('Title or resume'), max_length=128)
    url = models.CharField(verbose_name=('Online URL, app store link'), max_length=256, blank=True)
    logo = models.ImageField(verbose_name=('Logo'), blank=True, null=True)
    description = models.TextField(help_text=('Describe the software or feature and what your contribution was.'))
    release_date = models.DateField(verbose_name=('Release date'), blank=True, null=True)

    class Meta:
        verbose_name = ('User_Project')
        verbose_name_plural = ('User_Projects')
        ordering = ('-release_date',)

    def __str__(self):  
        return self.title



