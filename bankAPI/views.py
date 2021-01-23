from django.shortcuts import render
from .models import Branches
from rest_framework import viewsets
from .serializers import BranchSerializer
# Create your views here.


class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer