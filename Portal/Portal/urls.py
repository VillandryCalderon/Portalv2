from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from jobs.views import home
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required




urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('accounts.urls', namespace='accounts')),    
    path('QRPersonalizable/', include('QRPersonalizable.urls', namespace='QRPersonalizable')),  
    ######    
    path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"), 
    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    
    path('automatic-crud/',include('automatic_crud.urls')),
    
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
  


]

if settings.DEBUG:
  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
