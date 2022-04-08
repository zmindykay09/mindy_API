from rest_framework import serializers
from . models import vehicles

class vhcseriliazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vehicles
        fields = ('id', 'name', 'desc')