from django.db import models
from decimal import *
from random import randint
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class BaseModel(models.Model):

    class Meta:
        abstract = True  # specify this model as an Abstract Model
        app_label = 'sustainbackendapp'

class Badge(BaseModel):
    name = models.CharField(max_length=30)
    restaurant = models.IntegerField()


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
    score = models.IntegerField(default=randint(0,5))
    username = models.CharField(max_length=40, default="Anonymous")
    comment = models.CharField(max_length=300)
    waterUp = models.IntegerField(default=0)
    waterDown = models.IntegerField(default=0)
    wasteUp = models.IntegerField(default=0)
    wasteDown = models.IntegerField(default=0)
    localUp = models.IntegerField(default=0)
    localDown = models.IntegerField(default=0)
    vegetarianUp = models.IntegerField(default=0)
    vegetarianDown = models.IntegerField(default=0)


@receiver(post_save, sender=Review)
def update_votes(sender, instance, **kwargs):
    instance.waterDown = 1 - instance.waterUp
    instance.wasteDown = 1 - instance.wasteUp
    instance.localDown = 1 - instance.localUp
    instance.vegetarianDown = 1 - instance.vegetarianUp
    instance.save()
