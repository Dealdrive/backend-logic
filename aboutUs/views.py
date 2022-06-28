from django.shortcuts import render
from django.shortcuts import render
from django.template import context
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import About_Us
from .serializers import aboutUsSerializer
from rest_framework import status

# Create your views here.


class AboutUs(APIView):
    
    def get(self, request):
        abt_us = About_Us.objects.all()

        serializer= aboutUsSerializer(abt_us, many = True, context = {'request': request})

        pilpline = (serializer.data)

        
        return Response(pilpline, status= status.HTTP_200_OK)
        


    
    def post(self, request, *args, **kargs):
        serializer = aboutUsSerializer(data = request.data)
        if serializer.is_valid():
            pilpline = serializer.save()

            # project = (project_serilizer.data)

            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)




class Detailed(APIView):

    def get_data(self, pk):
        try:
            return About_Us.objects.get(id = pk)

        except About_Us.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        aboutId = self.get_data(pk)

        serializer = aboutUsSerializer(aboutId, context = {'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        aboutId = self.get_data(pk)

        serializer = aboutUsSerializer(aboutId,data = request.data)

        if serializer.is_valid():
            
            context = serializer.save()

            return Response(serializer.data, status = status.HTTP_200_OK)

        return Response(serializer.data, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def delete(self, request, pk):

        aboutId = self.get_data(pk)
        
        aboutId.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
        
