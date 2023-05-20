from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="Home"),


    path('create_post/', views.metricCreate.as_view()),
    path('metrics_get/', views.get_metrics, name='get_metrics'),
    

]
