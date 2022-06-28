from .import views
from django.urls import path


urlpatterns = [

    path('v1/api/blogs', views.Blogs.as_view()),
    path('v1/api/blog/<str:pk>', views.Detailed.as_view())

]