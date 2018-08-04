from rest_framework import serializers
from .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("__all__")




#
# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#         '',
#         '',
#         ''
#         )
#         model = models.Photo
