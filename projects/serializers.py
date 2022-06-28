from rest_framework import serializers
from .models import Project



class ProjectSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Project
        fields = ['id', 'pro_title','pro_link','img']