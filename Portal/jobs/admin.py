from django.contrib import admin

from .models import *

admin.site.register(Contact)
admin.site.register(JobListing)
admin.site.register(ApplyJob)



class JobListingAdmin(admin.ModelAdmin):
    search_fields =('title'), 
    list_display = ('title', 'user','category'),

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
            obj.save()

class ApplyJobAdmin(admin.ModelAdmin): 
    list_display = ('name', 'email','file','job','job_Id'),
    search_fields=('name',),
    autocomplete_fields =['job_Id']
    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
            obj.save()