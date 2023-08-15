from django.urls import path
from . import views

urlpatterns = [
    path('sell-property/', views.Sell_Property_Api.as_view()),
]
