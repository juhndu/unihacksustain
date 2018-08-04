from django.db import models

# Create your models here.


class BaseModel(models.Model):

    class Meta:
        abstract = True  # specify this model as an Abstract Model
        app_label = 'sustainbackendapp'


class Review(BaseModel):
    score = models.IntegerField(default=0)
    recycle =

class Restaurant(BaseModel):
    name = models.CharField(max_length=60, default=None)
    rating = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))

    reviews = models.ForeignKey
