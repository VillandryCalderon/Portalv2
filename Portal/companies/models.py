from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from uuslug import uuslug
from . import constants


# Create your models here.

class Company(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    url = models.URLField(verbose_name=_('URL'), blank=True)
    location = models.CharField(max_length=120, blank=True)
    coordinates = models.CharField(max_length=64, help_text='lat,lon', blank=True)
    summary = models.CharField(max_length=128)
    size = models.CharField(_('Company size'), max_length=64, choices=constants.COMPANY_SIZE)
    employees = models.CharField(_('Quantity of employees'), max_length=64, choices=constants.COMPANY_EMPLOYEES)

    # contact
    contact_name = models.CharField(('Contact name'), max_length=128)
    contact_email = models.CharField(('Contact email'), max_length=128)
    contact_phone = models.CharField(('Contact phone'), max_length=128)
    contact_position = models.CharField(('Contact position'), max_length=128)

    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ['name']

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=75)
    url = models.URLField(verbose_name=('URL'), blank=True)
    location = models.CharField(max_length=120, blank=True)
    coordinates = models.CharField(max_length=64, help_text='lat,lon', blank=True)
    summary = models.CharField(max_length=128, blank=True)
    size = models.CharField(('Company size'), max_length=64, choices=constants.COMPANY_SIZE, blank=True)
    employees = models.CharField(('Quantity of employees'), max_length=64, choices=constants.COMPANY_EMPLOYEES,blank=True)

    class Meta:
        verbose_name_plural = 'Organizations'
        ordering = ['name']

    def __str__(self):
        return self.name