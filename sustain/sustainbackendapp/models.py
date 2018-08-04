from django.db import models
from decimal import *


# Create your models here.


class BaseModel(models.Model):

    class Meta:
        abstract = True  # specify this model as an Abstract Model
        app_label = 'sustainbackendapp'

class Badge(BaseModel):
    name = models.CharField(max_length=30)


class Restaurant(BaseModel):
    name = models.CharField(max_length=60, default=None)
    rating = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    imgUrl = models.CharField(max_length=120, default=None)
    address = models.CharField(max_length=200)
    locality = models.CharField(max_length=60)
    lat = models.FloatField()
    long = models.FloatField()


class Review(BaseModel):
    restaurant = models.IntegerField()
    score = models.IntegerField()
    username = models.CharField(max_length=40, default="Anonymous")
    waterUp = models.IntegerField(default=0)
    waterDown = models.IntegerField(default=0)
    wasteUp = models.IntegerField(default=0)
    wasteDown = models.IntegerField(default=0)
    localUp = models.IntegerField(default=0)
    localDown = models.IntegerField(default=0)
    vegetarianUp = models.IntegerField(default=0)
    vegetarianDown = models.IntegerField(default=0)


class Comment(BaseModel):
    restaurant = models.IntegerField()
    username = models.CharField(max_length=40)
    comment = models.CharField(max_length=300)
