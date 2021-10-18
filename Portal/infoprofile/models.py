from django.db import models
from django.db import models
from django.contrib.auth.models import User,Group
from django.utils.translation import ugettext as _

from companies.models import Organization
from education.models import Certification
from education.models import Institution
from . import constants

# Create your models here.



class UserProfile(models.Model):
    #Registeruser = models.ForeignKey(User, on_delete=models.CASCADE)
  
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    Group = models.ForeignKey(Group,default=1,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday = models.DateField(_('Fecha Nacimiento'))
    email = models.EmailField()
    phone = models.CharField(_('Telefono'), max_length=16, blank=True)
    location = models.CharField(max_length=120, blank=True)
    coordinates = models.CharField(max_length=64, help_text='lat,lon', blank=True)
    salary_min = models.IntegerField(_('Salario Minimo'), help_text=_('₡'), blank=True, null=True)
    job_type = models.CharField(_('Preferencia de empleo'), max_length=32, choices=constants.JOB_TYPE,blank=True)
    type_of_contract = models.CharField('Tipo de Contrato', max_length=32,choices=constants.TYPE_OF_CONTRACT, blank=True)
    Createresumen=models.FileField(upload_to='Resumenpostulantes',verbose_name="Cargar Curriculum",blank=True,null=True)
    

    class Meta:
        verbose_name = _('Informacion de usuario')
        verbose_name_plural = _('Informacion de usuarios')

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)


class UserEducation(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_education')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    title = models.CharField(_('Grado'), max_length=64)
    start_date = models.DateField(_('Fecha Inicio'))
    end_date = models.DateField(_('Fecha Finalizacion'), blank=True, null=True)
    in_progress = models.BooleanField(default=False,verbose_name=_('En Progreso'))
    description = models.TextField()

    class Meta:
        verbose_name = _('Educación')
        verbose_name_plural = _('Educación')
        ordering = ('-start_date', '-end_date')

    def __str__(self):
        return self.title


class UserCertification(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    name = models.CharField(_('Certificado'), max_length=64)
    start_date = models.DateField(_('Fecha Inicio'))
    end_date = models.DateField(_('Fecha Finalizacion'), blank=True, null=True)
    in_progress = models.BooleanField(default=False,verbose_name=_('En Progreso'))

    class Meta:
        verbose_name = _('Certificaciónes')
        verbose_name_plural = _('Certificaciónes')
        ordering = ('-start_date', '-end_date')

    def __str__(self):
        return self.name


class UserJob(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(_('Titulole'), max_length=64)
    start_date = models.DateField(_('Fecha Inicio'))
    end_date = models.DateField(_('Fecha Finalizacion'), blank=True, null=True)
    in_progress = models.BooleanField(default=False,verbose_name=_('En Progreso'))

    class Meta:
        verbose_name = _('Trabajo')
        verbose_name_plural = _('Trabajos')
        ordering = ('-start_date', '-end_date')

    def __str__(self):
        return self.title


class UserURL(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    network = models.CharField(max_length=32, choices=constants.USER_LINKS)
    url = models.CharField(_('Profile url or Username'), max_length=64)

    class Meta:
        verbose_name = _('User Url')
        verbose_name_plural = _('User Urls')

    def __str__(self):
        return '{}: {}'.format(self.network, self.url)


class UserProject(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(_('Title or resume'), max_length=128)
    url = models.CharField(_('Online URL, app store link'), max_length=256, blank=True)
    logo = models.ImageField(_('Logo'), blank=True, null=True)
    description = models.TextField(help_text=_('Describe the software or feature and what your contribution was.'))
    release_date = models.DateField(_('Release date'), blank=True, null=True)

    # TODO: technologies
    # TODO: import from github

    class Meta:
        verbose_name = _('User Project')
        verbose_name_plural = _('User Projects')
        ordering = ('-release_date',)

    def __str__(self):
        return self.title
