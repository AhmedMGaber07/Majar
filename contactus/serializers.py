from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import ContactUs


class ContactUsSerializer(ModelSerializer):

    class Meta:
        model = ContactUs
        fields = ['title_en', 'description_en', 'phone', 'phone_icon',
                  'email', 'email_icon', 'link', 'location_en', 'location_icon']


"""

api/product/
api/sell-property
api/home/

"""
