from django.urls import path
from . import views

urlpatterns = [
    path('contact-us/', views.Contact_Us_Api.as_view()),
]







