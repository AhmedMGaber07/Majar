from django.contrib import admin
from .models import ContactForm, ContactUs, ZoomForm
# Register your models here.


@admin.register(ContactUs)
class ContactUs(admin.ModelAdmin):
    list_per_page = 20


@admin.register(ContactForm)
class ContactForm(admin.ModelAdmin):
    list_per_page = 20


@admin.register(ZoomForm)
class ZoomForm(admin.ModelAdmin):
    list_per_page = 20
