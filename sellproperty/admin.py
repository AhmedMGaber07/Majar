from django.contrib import admin
from .models import SellProperty
# Register your models here.


@admin.register(SellProperty)
class SellProperty(admin.ModelAdmin):
    list_per_page = 20
