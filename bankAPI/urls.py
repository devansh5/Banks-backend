from django.urls import path,include

from .views import BranchViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('banks',BranchViewSet)

urlpatterns=[
    path('api/',BranchViewSet.as_view({'get': 'list'}),name='Branches-detail'),

]