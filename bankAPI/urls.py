from django.urls import path,include
from .views import *
from rest_framework import routers

urlpatterns=[
    path('api/branches/',BranchViewSet.as_view({'get': 'list'}),name="branches_list"),
    path('api/branches/autocomplete/',BranchAutoViewSet.as_view({'get': 'list'}),name="branches_detail"),
]
