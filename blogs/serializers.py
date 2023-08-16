from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import BlogDescriptions,Blog


class BlogDescriptionsSerializer(ModelSerializer):
    class Meta:
        model = BlogDescriptions
        fields = ['paragraph_en']



class BlogSerializer(ModelSerializer):
    blog_descriptions = BlogDescriptionsSerializer()

    class Meta:
        model = Blog
        fields = ['id', 'name_en', 'image', 'blog_descriptions','writer_en','date']




