from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'institution', views.InstitutionViewSet)
router.register(r'certification', views.CertificationViewSet)
