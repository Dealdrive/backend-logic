
# from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from .models import Message





class MessageSerializer(serializers.Serializer):

    
    class Meta:
        model = Message
        fields = ['id', 'userName', 'userEmail','subject','message']

        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Message.objects.all(),
        #         fields=['userName', 'userEmail', 'subject','message'],
        #         message = 'this field is required'
        #     )
        # ]

       







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