"""Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from jobs.views import home
from django.conf import settings
from django.conf.urls.static import static


from django import urls

from django.conf.urls import url, include
from jobs.routers import DefaultRouter
from education.urls import router as router_education
from companies.urls import router as router_companies
#from infoprofile.forms import FormularioUser
#from infoprofile.urls import router as router_user_profile
from django.contrib.auth import views as auth_views
from users.views import formularioUserView


router = DefaultRouter()
router.extend(router_education)
router.extend(router_companies)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('accounts.urls', namespace='accounts')),    
    path('QRPersonalizable/', include('QRPersonalizable.urls', namespace='QRPersonalizable')),  
    
    path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"), 
    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    
    
    
    
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        
    path('RegistrarUsuario/', formularioUserView.index,name='RegistrarUsuario'),
    path('guardarusuario/', formularioUserView.index,name='guardarusuario'),    

]

if settings.DEBUG:
  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
