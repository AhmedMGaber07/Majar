from django.db import models

# Create your models here.


class ContactUs(models.Model):
    title_en = models.CharField(max_length=250)
    title_ar = models.CharField(max_length=250, null=True, blank=True)
    description_en = models.TextField(max_length=500)
    description_ar = models.TextField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=250)
    phone_icon = models.ImageField(upload_to='documents/')
    email = models.EmailField(max_length=254)
    email_icon = models.ImageField(upload_to='documents/')
    link = models.URLField(max_length=200)
    location_en = models.CharField(max_length=250)
    location_ar = models.CharField(max_length=250, null=True, blank=True)
    location_icon = models.ImageField(upload_to='documents/')

    def __str__(self):
        return 'Contact Us'

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"


class ContactForm(models.Model):
    contact_us = models.ForeignKey(
        ContactUs, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    subject = models.TextField(max_length=500)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=500)

    def __str__(self):
        return 'Contact Form'

    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Form"


class ZoomForm(models.Model):
    contact_us = models.ForeignKey(
        ContactUs, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return 'Zoom Form'

    class Meta:
        verbose_name = "Zoom Form"
        verbose_name_plural = "Zoom Form"
