from django.db import models

# Create your models here.


class BaseModel(models.Model):

    class Meta:
        abstract = True  # specify this model as an Abstract Model
        app_label = 'sustainbackendapp'


class Restaurant(BaseModel):
    name = models.CharField(max_length=60, default=None)
