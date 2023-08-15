from django.urls import path
from . import views

urlpatterns = [
    path('about-us/', views.About_Us_Api.as_view()),
]
