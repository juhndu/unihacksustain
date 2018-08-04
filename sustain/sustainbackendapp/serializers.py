from rest_framework import serializers
from .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    avg_rating = serializers.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        model = Restaurant
        fields = ('name','avg_rating','imgUrl')



#
# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#         '',
#         '',
#         ''
#         )
#         model = models.Photo
