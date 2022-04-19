from django.contrib import admin
from .models import *
from . import models


# Register your models here.


class UserEducationInline(admin.TabularInline):
    model = models.UserEducation
    extra = 0


class UserCertificationInline(admin.TabularInline):
    model = models.UserCertification
    extra = 0


class UserJobInline(admin.TabularInline):
    model = models.UserJob
    extra = 0


class UserURLInline(admin.TabularInline):
    model = models.UserURL
    extra = 0


class UserProjectInline(admin.TabularInline):
    model = models.UserProject
    extra = 0





@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name','email','phone','Createresumen')
    inlines = [UserEducationInline, UserCertificationInline, UserJobInline, UserURLInline, UserProjectInline]
