from django.shortcuts import render
from django.http import HttpResponse
from .models import metric
import csv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime

# # Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
#here i have using @apiview

@api_view(['GET'])
def get_metrics(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    metrics = metric.objects.filter(time__range=(start, end))
    print(metrics)
    #data set
    data = [
        {'time': metric.time, 'voltage': metric.voltage, 'current': metric.current}
        for metric in metrics
    ]
    return Response(data)



# Here i have using generic views with serialization >- it provide sort method for create Apis

from .serializers import metricSerializer
from rest_framework.generics import CreateAPIView


class metricCreate(CreateAPIView):
    queryset = metric.objects.all()
    serializer_class = metricSerializer