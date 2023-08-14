from django.contrib import admin
from .models import ContactForm, ContactUs, ZoomForm
# Register your models here.


class ContactFormInline(admin.StackedInline):
    model = ContactForm


class ZoomFormInline(admin.StackedInline):
    model = ZoomForm


@admin.register(ContactUs)
class ContactUs(admin.ModelAdmin):
    list_per_page = 20
    inlines = [ContactFormInline, ZoomFormInline]
