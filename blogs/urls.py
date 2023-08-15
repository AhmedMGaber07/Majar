from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.Blogs_Api.as_view()),
]
