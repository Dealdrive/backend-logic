from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status

# Create your views here.


class Blogs(APIView):
    
    def get(self, request):
        abt_us = Blog.objects.all()

        serializer= BlogSerializer(abt_us, many = True, context = {'request': request})

        pipeline = (serializer.data)

        
        return Response(pipeline, status= status.HTTP_200_OK)
        


    
    def post(self, request, *args, **kargs):
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
            pilpline = serializer.save()

            # project = (project_serilizer.data)

            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)




class Detailed(APIView):

    def get_data(self, pk):
        try:
            return Blog.objects.get(id = pk)

        except Blog.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        aboutId = self.get_data(pk)

        serializer = BlogSerializer(aboutId, context = {'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        aboutId = self.get_data(pk)
        serializer = BlogSerializer(aboutId,data = request.data)
        if serializer.is_valid():     
            context = serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.data, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def delete(self, request, pk):

        aboutId = self.get_data(pk)
        
        aboutId.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
        
