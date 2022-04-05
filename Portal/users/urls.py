from django.urls import path
from .views import *
from users import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views

from django.contrib.auth.decorators import login_required
#from users.views import UserEditView


router = DefaultRouter()
#router.register(r'userprofile', views.UserProfileViewSet)

app_name = 'users'

urlpatterns = [

 #   path('userprofile/', UserProfileViewSet, name='userprofile'),
 #   path('edit_profile/', UserEditView.as_view(), name='edit_profile'),   
 #   path('edit2/', UserProfileViewSet , name='edit2'),   
    
    
]


