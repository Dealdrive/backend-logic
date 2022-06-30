
from django.forms import CharField
from rest_framework import serializers
from .models import Message


def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')


class MessageSerializer(serializers.ModelSerializer):

    subject = CharField(validators=[required])


    class Meta:
        model = Message
        fields = ['id', 'userName', 'userEmail','subject','message']

        # extra_kwargs = {'userName': {'required': True, 'allow_blank': False}}
        # extra_kwargs = {'userEmail': {'required': True,'allow_blank': False}}
        # extra_kwargs = {'subject': {'required': True,'allow_blank': False}}
        # extra_kwargs = {'message': {'required': True,'allow_blank': False}}







# class SignupSerializer(serializers.ModelSerializer):
#         """ Serializer User Signup """
#         class Meta:
#             model = User
#             fields = ['username', 'password', 'password', 'first_name', 'last_name', 'email']
            
#             extra_kwargs = {'first_name': {'required': True, 'allow_blank': False}}
#             extra_kwargs = {'last_name': {'required': True,'allow_blank': False}}
#             extra_kwargs = {'email': {'required': True,'allow_blank': False}}


# def required(value):
#     if value is None:
#         raise serializers.ValidationError('This field is required')

# class GameRecord(serializers.ModelSerializer):
#     score = IntegerField(validators=[required])

#     class Meta:
#         model = Game