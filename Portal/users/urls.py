from django.urls import path
from .views import *
from users import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views
from jobs.views import home
from django.contrib.auth.decorators import login_required
#from users.views import UserEditView
router = DefaultRouter()

app_name = 'users'
urlpatterns = [
 
    
 
    
    
]
