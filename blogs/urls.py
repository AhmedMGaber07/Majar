from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.Blog_Api.as_view()),
]
