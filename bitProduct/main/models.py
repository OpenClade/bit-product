from django.db import models

# Create your models here.


class Product(models.Model):
    website = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    price_avg = models.FloatField(null=True)
    sallers = models.IntegerField(null=True)
    name_short_shop = models.CharField(max_length=255, null=True) 
    name_long_shop = models.CharField(max_length=255, null=True)
    links = models.CharField(max_length=255, null=True)
    
    # dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name