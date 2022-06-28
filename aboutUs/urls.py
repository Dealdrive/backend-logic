from .import views
from django.urls import path


urlpatterns = [

    path('v1/api/aboutUs', views.AboutUs.as_view()),
    path('v1/api/aboutUs/<str:pk>', views.Detailed.as_view())

]