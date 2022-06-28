from django.shortcuts import render
from django.shortcuts import render
from django.template import context
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import status

# Create your views here.


class Projects(APIView):
    
    def get(self, request):
        projects = Project.objects.all()

        project_serilizer= ProjectSerializer(projects, many = True, context = {'request': request})

        project = (project_serilizer.data)

        if(project):
            return Response(project, status= status.HTTP_200_OK)
        return Response(project, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


    
    def post(self, request, *args, **kargs):
        project_serilizer = ProjectSerializer(data = request.data)
        if project_serilizer.is_valid():
            project = project_serilizer.save()

            # project = (project_serilizer.data)

            return Response(project_serilizer.data, status = status.HTTP_201_CREATED)
        return Response(project_serilizer.data, status = status.HTTP_400_BAD_REQUEST)




class singleProject(APIView):

    def get_data(self, pk):
        try:
            return Project.objects.get(id = pk)

        except Project.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        projectId = self.get_data(pk)

        project_serilizer = ProjectSerializer(projectId, context = {'request': request})

        return Response(project_serilizer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        projectId = self.get_data(pk)

        project_serializer = ProjectSerializer(projectId,data = request.data)

        if project_serializer.is_valid():
            
            context = project_serializer.save()

            return Response(project_serializer.data, status = status.HTTP_200_OK)

        return Response(project_serializer.data, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def delete(self, request, pk):

        projectId = self.get_data(pk)
        
        projectId.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
        
