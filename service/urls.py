from .import views 
from django.urls import path

urlpatterns = [

    path('v1/api/cats', views.Categories.as_view()),
    path('v1/api/cat/<str:pk>', views.Detailed_Cat.as_view()),

    path('v1/api/paks', views.Packages.as_view()),
    path('v1/api/paks/<str:pk>', views.Detailed_pak.as_view()),


]