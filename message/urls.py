from .import views
from django.urls import path


urlpatterns = [


    path('v1/api/messages', views.Messages.as_view())


]