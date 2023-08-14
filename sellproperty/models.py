from django.db import models

# Create your models here.


class SellProperty(models.Model):
    Name = models.CharField(max_length=250)
    Phone = models.CharField(max_length=250)
    Location = models.CharField(max_length=250)
    Area = models.PositiveIntegerField()
    Type = models.CharField(max_length=250)
    

    def __str__(self):
        return 'Sell Property'

    class Meta:
        verbose_name = "Sell Property"
        verbose_name_plural = "Sell Property"
