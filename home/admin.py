from django.contrib import admin
from .models import Home, HomeSlider, WhatWeProvides
# Register your models here.


class HomeSliderInline(admin.StackedInline):
    model = HomeSlider


class WhatWeProvidesInline(admin.StackedInline):
    model = WhatWeProvides


@admin.register(Home)
class Home(admin.ModelAdmin):
    list_per_page = 20
    inlines = [WhatWeProvidesInline, HomeSliderInline]
