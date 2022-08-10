from pyexpat import model
from rest_framework import serializers
from .models import Pokemon


class ListSerializer(serializers.Serializer):
    class Meta:
        model = Pokemon
        field = ['name', 'type']
        
        
        #to exclude we use exlude = ("type")