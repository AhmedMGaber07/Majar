from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import ContactUs
from .serializers import ContactUsSerializer

# Create your views here.


class Contact_Us_Api(APIView):

    def get_object(self, id):
        try:
            return ContactUs.objects.get(id=id)
        except ContactUs.DoesNotExist:
            raise Response('ContuctUs Does Not Exist')

    def get(self, request, format=None):
        contactus = ContactUs.objects.all()
        serializer = ContactUsSerializer(contactus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        # Create a new con object
        contactus = ContactUs.objects.create(
            title_en=data['title_en'],
            description_en=data['description_en'],
            phone=data['phone'],
            phone_icon=data['phone_icon'],
            email=data['email'],
            email_icon=data['email_icon'],
            link=data['link'],
            location_en=data['location_en'],
            location_icon=data['location_icon'],
        )

        # Save the con object
        contactus.save()

        # Return the con object
        return Response(contactus.data)
