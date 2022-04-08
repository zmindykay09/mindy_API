from django.http import QueryDict
from django.shortcuts import render
from rest_framework import viewsets
from . serializers import vhcseriliazer
from . models import vehicles

class vehicleviewset(viewsets.ModelViewSet):
    queryset = vehicles.objects.all().order_by('name')
    serializer_class = vhcseriliazer

# Create your views here.
