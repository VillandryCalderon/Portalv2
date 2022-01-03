
from django.urls import path
from .views import *
from jobs import views
from django.conf import settings
from django.conf.urls.static import static
#from infoprofile.views import formularioUserView

app_name = 'jobs'

urlpatterns = [

    path('contact/', contact, name='contact'),
    path('about/', about_us, name='about'),
    path('service/', service, name='service'),
    path('job-post/', job_post, name='job-post'),
    path('job-listing/', job_listing, name='job-listing'),
    path('job-single/<int:id>/', job_single, name='job-single'),
    path('search/', SearchView.as_view(), name='search'),
    path('apply/', apply_job, name='apply'),
    path('ApplyJobListing/', jobapply_listing, name='ApplyJobListing'),
   #path('ApplyJobListing/', ApplyJobListing, name='ApplyJobListing'),
    



]


