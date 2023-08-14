from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Call)
class Call(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_per_page = 20


@admin.register(DeliveryConditions)
class DeliveryConditions(admin.ModelAdmin):
    list_per_page = 20


@admin.register(DeliveryTypes)
class DeliveryTypes(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Developers)
class Developers(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Locations)
class Locations(admin.ModelAdmin):
    list_per_page = 20


@admin.register(PopularDevelopers)
class PopularDevelopers(admin.ModelAdmin):
    list_per_page = 20


@admin.register(PopularLocations)
class PopularLocations(admin.ModelAdmin):
    list_per_page = 20


class PlansInline(admin.StackedInline):
    model = Plans


class AmenitiesInline(admin.StackedInline):
    model = Amenities


class PropertyImagesInline(admin.StackedInline):
    model = PropertyImages


@admin.register(General)
class General(admin.ModelAdmin):
    list_per_page = 20
    inlines = [PlansInline, AmenitiesInline, PropertyImagesInline]


class PropertySubTypesInline(admin.StackedInline):
    model = PropertySubTypes


@admin.register(PropertyTypes)
class PropertyTypes(admin.ModelAdmin):
    list_per_page = 20
    inlines = [PropertySubTypesInline]


@admin.register(PropertySubTypes)
class PropertySubTypes(admin.ModelAdmin):
    list_per_page = 20
