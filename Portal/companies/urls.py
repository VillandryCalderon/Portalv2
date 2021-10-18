from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'organization', views.OrganizationViewSet)
