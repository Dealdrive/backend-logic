from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Package
from .serializers import CategorySerializer, PackageSerializer, DetailedPackageSerializer
from rest_framework import status



class Categories(APIView):
    
    def get(self, request):
        cat = Category.objects.all()
        serializer = CategorySerializer(cat, many=True, context={'request':request})
        pipeline=({ 'cats':serializer.data })

        return Response(pipeline, status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            save = serializer.save()

            return Response({ 'cats':serializer.data }, status = status.HTTP_201_CREATED)
        return Response({ 'cats':serializer.data }, status=status.HTTP_400_BAD_REQUEST)


class Detailed_Cat(APIView):
    def get_data(self, pk):
        try:
            return Category.objects.get(id = pk)

        except Category.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        cat = self.get_data(pk)
        serializer = CategorySerializer(cat, context={'request':request})
        return Response({ 'cats':serializer.data }, status = status.HTTP_200_OK)


    def put(self, request, pk):
        cat = self.get_data(pk)
        serializer = CategorySerializer(cat, data = request.data)
        if serializer.is_valid():
            save = serializer.save()
            return Response({ 'cats':serializer.data }, status = status.HTTP_201_CREATED)
        return Response({ 'cats':serializer.data }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, pk):
        cat = self.get_data(pk)
        cat.delete()
        return Response({'detail':'Category is Deleted'})





class Packages(APIView):
    
    def get(self, request):
        pak = Package.objects.all()
        serializer = DetailedPackageSerializer(pak, many=True, context={'request':request})
        pipeline=({ 'paks':serializer.data })

        return Response(pipeline, status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = PackageSerializer(data = request.data)
        if serializer.is_valid():
            save = serializer.save()

            return Response({ 'paks':serializer.data }, status = status.HTTP_201_CREATED)
        return Response({ 'paks':serializer.data }, status=status.HTTP_400_BAD_REQUEST)


class Detailed_pak(APIView):
    def get_data(self, pk):
        try:
            return Package.objects.get(id = pk)

        except Package.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        pak = self.get_data(pk)
        serializer = DetailedPackageSerializer(pak, context={'request':request})
        return Response({ 'paks':serializer.data }, status = status.HTTP_200_OK)


    def put(self, request, pk):
        pak = self.get_data(pk)
        serializer = PackageSerializer(pak, data = request.data)
        if serializer.is_valid():
            save = serializer.save()
            return Response({ 'paks':serializer.data }, status = status.HTTP_201_CREATED)
        return Response({ 'paks':serializer.data }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, pk):
        pak = self.get_data(pk)
        pak.delete()
        return Response({'detail':'Category is Deleted'})
