from django.db import models

# Create your models here.


class Header(models.Model):

    title_en = models.CharField(max_length=250)
    title_ar = models.CharField(
        max_length=250, null=True, blank=True)
    description_en = models.TextField(max_length=500)
    description_ar = models.TextField(
        max_length=500, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return 'About Us'

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Mission(models.Model):
    header = models.ForeignKey(
        Header, on_delete=models.SET_NULL, null=True, blank=True)
    title_en = models.CharField(max_length=250)
    title_ar = models.CharField(
        max_length=250, null=True, blank=True)
    description_en = models.TextField(max_length=500)
    description_ar = models.TextField(
        max_length=500, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return 'Mission'

    class Meta:
        verbose_name = "Mission"
        verbose_name_plural = "Mission"

class Vision(models.Model):
    header = models.ForeignKey(
        Header, on_delete=models.SET_NULL, null=True, blank=True)
    title_en = models.CharField(max_length=250)
    title_ar = models.CharField(
        max_length=250, null=True, blank=True)
    description_en = models.TextField(max_length=500)
    description_ar = models.TextField(
        max_length=500, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return 'Vision'

    class Meta:
        verbose_name = "Vision"
        verbose_name_plural = "Vision"

class WhyUs(models.Model):
    header = models.ForeignKey(
        Header, on_delete=models.SET_NULL, null=True, blank=True)
    description_en = models.TextField(max_length=500)
    description_ar = models.TextField(
        max_length=500, null=True, blank=True)

    def __str__(self):
        return 'Why Us'

    class Meta:
        verbose_name = "Why Us"
        verbose_name_plural = "Why Us"

class CustomHotline(models.Model):
    header = models.ForeignKey(
        Header, on_delete=models.SET_NULL, null=True, blank=True)
    title_en = models.CharField(max_length=250)
    title_ar = models.CharField(
        max_length=250, null=True, blank=True)
    sub_title_en = models.CharField(max_length=250)
    sub_title_ar = models.CharField(
        max_length=250, null=True, blank=True)
    custom_hotline_phone = models.PositiveIntegerField()

    def __str__(self):
        return 'Custom Hotline'

    class Meta:
        verbose_name = "Custom Hotline"
        verbose_name_plural = "Custom Hotline"


class Property(models.Model):
    header = models.ForeignKey(
        Header, on_delete=models.SET_NULL, null=True, blank=True)
    title_en = models.CharField(max_length=250)
    title_ar = models.CharField(
        max_length=250, null=True, blank=True)
    description_en = models.TextField(max_length=500)
    description_ar = models.TextField(
        max_length=500, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return 'Property'

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Property"

        

class Contact(models.Model):
    header = models.ForeignKey(
        Header, on_delete=models.SET_NULL, null=True, blank=True)
    title_en = models.CharField(max_length=250)
    title_ar = models.CharField(
        max_length=250, null=True, blank=True)
    description_en = models.TextField(max_length=500)
    description_ar = models.TextField(
        max_length=500, null=True, blank=True)
    icon = models.ImageField()
    image = models.ImageField()
    background = models.ImageField()

    def __str__(self):
        return 'Contact'

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"


class WhyMajar(models.Model):
    header = models.ForeignKey(
        Header, on_delete=models.SET_NULL, null=True, blank=True)
    title_en = models.CharField(max_length=250)
    title_ar = models.CharField(
        max_length=250, null=True, blank=True)
    icon = models.ImageField()
    description_en = models.TextField(max_length=500)
    description_ar = models.TextField(
        max_length=500, null=True, blank=True)
    

    def __str__(self):
        return 'Why Majar'

    class Meta:
        verbose_name = "Why Majar"
        verbose_name_plural = "Why Majar"