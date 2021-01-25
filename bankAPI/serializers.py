from .models import Branches
from rest_framework import serializers


class BranchSerializer(serializers.ModelSerializer):
    bank_name=serializers.CharField(source='bank.name')
    class Meta:
        model = Branches
        fields = ['ifsc','bank_name','branch','address','city','district','state']
