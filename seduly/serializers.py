from rest_framework import serializers
from .models import *




class metricSerializer(serializers.ModelSerializer):
    class Meta:
        model = metric
        fields = ['time','voltage','current']
