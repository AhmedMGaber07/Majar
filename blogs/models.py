from django.db import models
from Property.models import General
# Create your models here.


class Blog(models.Model):
    name_en = models.CharField(max_length=250)
    name_ar = models.CharField(
        max_length=250, null=True, blank=True)
    writer_en = models.CharField(max_length=250)
    writer_ar = models.CharField(
        max_length=250, null=True, blank=True)
    date = models.DateField()
    image = models.ImageField()
    related_properties = models.ForeignKey(
        General, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return 'Blog'

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"


class BlogDescriptions(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.SET_NULL, null=True, blank=True)
    paragraph_en = models.TextField(max_length=500)
    paragraph_ar = models.TextField(max_length=500, null=True, blank=True)
    list_items_en = models.TextField(max_length=500)
    list_items_ar = models.TextField(max_length=500, null=True, blank=True)
    order = models.PositiveIntegerField()

    def __str__(self):
        return 'Blog Descriptions'

    class Meta:
        verbose_name = "Blog Descriptions"
        verbose_name_plural = "Blog Descriptions"
