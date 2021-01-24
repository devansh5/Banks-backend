from django.shortcuts import render
from .models import Branches
from rest_framework import viewsets,filters
from .serializers import BranchSerializer

# Create your views here.


class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    search_fields= ['=branch','=city','=ifsc','=state','=bank__id']
    ordering_fields=['ifsc']
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer

class BranchAutoViewSet(viewsets.ModelViewSet):
    search_fields=['branch',]
    filter_backends=(filters.SearchFilter,)
    queryset=Branches.objects.all()
    serializer_class=BranchSerializer

    