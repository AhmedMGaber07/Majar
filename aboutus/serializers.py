from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import *


class MissionSerializer(ModelSerializer):
    class Meta:
        model = Mission
        fields = ['title_en', 'description_en', 'image']


class VisionSerializer(ModelSerializer):
    class Meta:
        model = Vision
        fields = ['title_en', 'description_en', 'image']


class WhyUsSerializer(ModelSerializer):
    class Meta:
        model = WhyUs
        fields = ['why_majar_title_en']


class CustomHotlineSerializer(ModelSerializer):
    class Meta:
        model = CustomHotline
        fields = ['title_en', 'sub_title_en', 'custom_hotline_phone']


class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = ['title_en', 'description_en', 'image']


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['title_en', 'description_en', 'icon', 'image', 'background']


class WhyMajarSerializer(ModelSerializer):
    class Meta:
        model = WhyMajar
        fields = ['title_en', 'icon', 'description_en']


class AboutUsSerializer(ModelSerializer):
    mission = MissionSerializer()
    vision = VisionSerializer()
    why_us = WhyUsSerializer()
    custom_hotline = CustomHotlineSerializer()
    property_ = PropertySerializer()
    contact = ContactSerializer()
    why_majar = WhyMajarSerializer()

    class Meta:
        model = Header
        fields = ['title_en', 'description_en', 'image', 'mission', 'vision',
                  'why_us', 'custom_hotline', 'property_', 'contact', 'why_majar']
