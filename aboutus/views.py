from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Header
from .serializers import AboutUsSerializer

# Create your views here.


class About_Us_Api(APIView):

    def get_object(self, id):
        try:
            return Header.objects.get(id=id)
        except Header.DoesNotExist:
            raise Response('AboutUs Does Not Exist')

    def get(self, request, format=None):
        about_us = Header.objects.all()
        serializer = AboutUsSerializer(about_us, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        # Create a new con object
        about_us = Header.objects.create(
            title_en=data['title_en'],
            description_en=data['description_en'],
            image=data['image'],
            mission=data['mission'],
            vision=data['vision'],
            why_us=data['why_us'],
            custom_hotline=data['custom_hotline'],
            property_=data['property_'],
            contact=data['contact'],
            why_majar=data['why_majar'],

        )

        # Save the con object
        about_us.save()

        # Return the con object
        return Response(about_us.data)
