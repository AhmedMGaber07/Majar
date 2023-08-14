from django.contrib import admin
from .models import Header, Mission, Vision, WhyUs, CustomHotline, Property, Contact, WhyMajar

# Register your models here.


class MissionInline(admin.StackedInline):
    model = Mission


class VisionInline(admin.StackedInline):
    model = Vision


class WhyUsInline(admin.StackedInline):
    model = WhyUs


class CustomHotlineInline(admin.StackedInline):
    model = CustomHotline


class PropertyInline(admin.StackedInline):
    model = Property


class ContactInline(admin.StackedInline):
    model = Contact


class WhyMajarInline(admin.StackedInline):
    model = WhyMajar


@admin.register(Header)
class Header(admin.ModelAdmin):
    list_per_page = 20
    inlines = [MissionInline, VisionInline, WhyUsInline,
               CustomHotlineInline, PropertyInline, ContactInline, WhyMajarInline]
