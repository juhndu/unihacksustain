from django.shortcuts import render
from .models import *
from .serializers import *

# Create your views here.

class PhotoList(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = Restaurant.objects.order_by('?')
        return queryset
