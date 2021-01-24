from .models import Branches
from rest_framework import serializers


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ['ifsc','bank','branch','address','city','district','state']
