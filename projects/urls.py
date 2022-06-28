from .import views
from django.urls import path


urlpatterns = [

    path('v1/api/projects', views.Projects.as_view()),
    path('v1/api/projects/<str:pk>', views.singleProject.as_view())

]