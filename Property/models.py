from django.db import models

# Create your models here.


class Call(models.Model):
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)

    def __str__(self):
        return 'Call'

    class Meta:
        verbose_name = "Call"
        verbose_name_plural = "Call"


class Category(models.Model):
    name_en = models.CharField(max_length=254)
    name_ar = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return 'Category'

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"


class DeliveryConditions(models.Model):
    name_en = models.CharField(max_length=254)
    name_ar = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return 'Delivery Conditions'

    class Meta:
        verbose_name = "Delivery Conditions"
        verbose_name_plural = "Delivery Conditions"


class DeliveryTypes(models.Model):
    name_en = models.CharField(max_length=254)
    name_ar = models.CharField(max_length=254, null=True, blank=True)
    year = models.DateField()

    def __str__(self):
        return 'Delivery Types'

    class Meta:
        verbose_name = "Delivery Types"
        verbose_name_plural = "Delivery Types"


class Developers(models.Model):
    name_en = models.CharField(max_length=254)
    name_ar = models.CharField(max_length=254, null=True, blank=True)
    logo = models.ImageField()

    def __str__(self):
        return 'Developers'

    class Meta:
        verbose_name = "Developers"
        verbose_name_plural = "Developers"


class Locations(models.Model):
    name_en = models.CharField(max_length=254)
    name_ar = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return 'Locations'

    class Meta:
        verbose_name = "Locations"
        verbose_name_plural = "Locations"


class PopularDevelopers(models.Model):
    developer = models.ForeignKey(
        Developers, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Popular Developers'

    class Meta:
        verbose_name = "Popular Developers"
        verbose_name_plural = "Popular Developers"


class PopularLocations(models.Model):
    Location = models.ForeignKey(
        Locations, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Popular Locations'

    class Meta:
        verbose_name = "Popular Locations"
        verbose_name_plural = "Popular Locations"


class PropertyTypes(models.Model):
    name_en = models.CharField(max_length=254)
    name_ar = models.CharField(max_length=254, null=True, blank=True)
    logo = models.ImageField()

    def __str__(self):
        return 'Property Types'

    class Meta:
        verbose_name = "Property Types"
        verbose_name_plural = "Property Types"


class PropertySubTypes(models.Model):
    type = models.ForeignKey(
        PropertyTypes, on_delete=models.CASCADE, null=True, blank=True)
    name_en = models.CharField(max_length=254)
    name_ar = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return 'Property Sub Types'

    class Meta:
        verbose_name = "Property Sub Types"
        verbose_name_plural = "Property Sub Types"


class General(models.Model):
    name_en = models.CharField(max_length=250)
    name_ar = models.CharField(
        max_length=250, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    location = models.ForeignKey(
        PopularLocations, on_delete=models.CASCADE)
    Type = models.ForeignKey(
        PropertySubTypes, on_delete=models.CASCADE)
    delivery_type = models.ForeignKey(
        DeliveryTypes, on_delete=models.CASCADE)
    delivery_condition = models.ForeignKey(
        DeliveryConditions, on_delete=models.CASCADE)
    developed_by = models.ForeignKey(
        PopularDevelopers, on_delete=models.CASCADE)
    call = models.ForeignKey(
        Call, on_delete=models.CASCADE)
    bedroom_number = models.PositiveIntegerField()
    bathroom_number = models.PositiveIntegerField()
    move_now_pay_later = models.BooleanField(default=False)
    area = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description_en = models.TextField(max_length=500)
    description_ar = models.TextField(max_length=500, null=True, blank=True)
    floor_plan = models.URLField()
    master_plan = models.URLField()
    location_link = models.TextField(max_length=500)
    show_in_home_page = models.BooleanField(default=False)

    def __str__(self):
        return 'Properties'

    class Meta:
        verbose_name = "Properties"
        verbose_name_plural = "Properties"


class Plans(models.Model):
    Properties = models.ForeignKey(
        General, on_delete=models.CASCADE, null=True, blank=True)
    down_price = models.PositiveIntegerField()
    monthly_instalments = models.PositiveIntegerField()
    instalment_years = models.PositiveIntegerField()
    delivery_payment = models.PositiveIntegerField()

    def __str__(self):
        return 'Plans'

    class Meta:
        verbose_name = "Plans"
        verbose_name_plural = "Plans"


class Amenities(models.Model):
    Properties = models.ForeignKey(
        General, on_delete=models.CASCADE, null=True, blank=True)
    clubhouse = models.BooleanField(default=False)
    schools = models.BooleanField(default=False)
    medical_center = models.BooleanField(default=False)
    commercial_strip = models.BooleanField(default=False)
    business_hub = models.BooleanField(default=False)
    sports_clubs = models.BooleanField(default=False)
    bicycles_lanes = models.BooleanField(default=False)
    jogging_trail = models.BooleanField(default=False)

    def __str__(self):
        return 'Amenities'

    class Meta:
        verbose_name = "Amenities"
        verbose_name_plural = "Amenities"


class PropertyImages(models.Model):
    Properties = models.ForeignKey(
        General, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField()
    is_main = models.BooleanField(default=False)

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')

    def __str__(self):
        return 'Property Images'

    class Meta:
        verbose_name = "Property Images"
        verbose_name_plural = "Property Images"
