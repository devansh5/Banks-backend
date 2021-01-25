from django.shortcuts import render
from .models import Branches
from rest_framework import viewsets,filters
from .serializers import BranchSerializer

# Create your views here.

# search across all fields
class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    search_fields= ['branch','city','district','address','ifsc','state','bank__name']
    ordering_fields=['ifsc']
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer

# autocomplete api for searching over branches
class BranchAutoViewSet(viewsets.ModelViewSet):
    search_fields=['branch',]
    filter_backends=(filters.SearchFilter,)
    queryset=Branches.objects.all()
    serializer_class=BranchSerializer

    