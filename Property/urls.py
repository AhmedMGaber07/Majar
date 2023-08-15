from django.urls import path
from . import views

urlpatterns = [
    path('property/', views.Property_Api.as_view()),
]
