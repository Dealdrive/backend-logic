from rest_framework import serializers
from .models import About_Us



class aboutUsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = About_Us
        fields = ['id', 'body','img']