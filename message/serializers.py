
# from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from .models import Message





class MessageSerializer(serializers.Serializer):

    
    class Meta:
        model = Message
        fields = ['id', 'userName', 'userEmail','subject','message']

        