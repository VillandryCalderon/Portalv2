from django.urls import path
from .views import *
from users import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'userprofile', views.UserProfileViewSet)

app_name = 'users'

urlpatterns = [

    path('userprofile/', formularioUserView, name='userprofile'),
]


