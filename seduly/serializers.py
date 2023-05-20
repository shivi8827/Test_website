from rest_framework import serializers
from .models import *
#from django.contrib.auth.hashers import make_password



class metricSerializer(serializers.ModelSerializer):
    class Meta:
        model = metric
        fields = ['time','voltage','current']
