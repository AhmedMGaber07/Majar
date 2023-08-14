from django.contrib import admin
from .models import Blog, BlogDescriptions

# Register your models here.


class BlogDescriptionsInline(admin.StackedInline):
    model = BlogDescriptions


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_per_page = 20
    inlines = [BlogDescriptionsInline]
