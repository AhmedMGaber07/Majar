from django.db import models

# Create your models here.


class Home(models.Model):
    what_we_provide_title_en = models.CharField(max_length=250)
    what_we_provide_title_ar = models.CharField(
        max_length=250, null=True, blank=True)
    contact_title_en = models.CharField(max_length=250)
    contact_title_ar = models.CharField(
        max_length=250, null=True, blank=True)
    contact_description_en = models.TextField(max_length=500)
    contact_description_ar = models.TextField(
        max_length=500, null=True, blank=True)
    contact_image = models.ImageField()
    contact_background = models.ImageField()
    recommend_properties_title_en = models.CharField(max_length=250)
    recommend_properties_title_ar = models.CharField(
        max_length=250, null=True, blank=True)

    def __str__(self):
        return 'Home'

    class Meta:
        verbose_name = "General"
        verbose_name_plural = "Home"


class WhatWeProvides(models.Model):
    home = models.ForeignKey(
        Home, on_delete=models.SET_NULL, null=True, blank=True)
    icon = models.ImageField(upload_to='documents/')
    name_en = models.CharField(max_length=250)
    name_ar = models.CharField(max_length=250, null=True, blank=True)
    description_en = models.TextField(max_length=500)
    description_ar = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return 'What We Provides'

    class Meta:
        verbose_name = "What We Provides"
        verbose_name_plural = "What We Provides"


class HomeSlider(models.Model):
    home = models.ForeignKey(
        Home, on_delete=models.SET_NULL, null=True, blank=True)
    Video_or_image = models.FileField(
        upload_to='documents/', null=True, blank=True)

    def __str__(self):
        return 'Home Slider'

    class Meta:
        verbose_name = "Home Slider"
        verbose_name_plural = "Home Slider"
