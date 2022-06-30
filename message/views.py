from pyexpat.errors import messages
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message
from .serializers import MessageSerializer
from rest_framework import status


class Messages(APIView):

    def get(self, request, *args, **kwargs):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages,many = True, context = {'request':request})
        pipeline = (serializer.data)

        return Response(pipeline, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            save = serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        