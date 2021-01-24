from django.urls import path,include

from .views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router=routers.SimpleRouter()
router.register(r'api/branches',BranchViewSet)
router.register(r'autocomplete',BranchAutoViewSet)
urlpatterns=router.urls