from .models import *
from .serializers import *
from .forms import *
from django.shortcuts import render
from django.db.models import Avg, Sum
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from math import radians, cos, sin, asin, sqrt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
import requests
from random import randint


# Create your views here.

#def comments(request, resto_id):

@api_view(['POST'])
def submitReview(request, rid):
    print(request.data)
    form = ReviewForm(request.data)
    if form.is_valid():
        print("valid")
        form.save()
        return Response("ok")
    return Response("failed")

def genReviews(id):
    for i in range(0,10):
        water = randint(0,1)
        waste = randint(0,1)
        loca = randint(0,1)
        vege = randint(0,10)
        if(vege>7):
            vege=0
        rev = Review.objects.create(restaurant=id,score=randint(0,5),waterUp=water,wasteUp=waste,localUp=loca,vegetarianUp=vege)
    return

def scoreReviews(id):
    revScores = {}
    Badge.objects.filter(restaurant=id).delete()
    reviews = Review.objects.filter(restaurant=id)
    Badge
    wasteUps = 0
    wasteDowns = 0
    localUps = 0
    localDowns = 0
    waterUps = 0
    waterDowns = 0
    vegUps = 0
    vegDowns = 0
    for r in reviews:
        wasteUps+=r.wasteUp
        wasteDowns+=r.wasteDown
        localUps+=r.localUp
        localDowns+=r.localDown
        waterUps+=r.waterUp
        waterDowns+=r.waterDown
        vegUps+=r.vegetarianUp
        vegDowns+=r.vegetarianDown
    revScores['waste']=float(wasteUps)/(float(wasteUps)+float(wasteDowns))
    revScores['water']=float(waterUps)/(float(waterUps)+float(waterDowns))
    revScores['veg']=float(vegUps)/(float(vegUps)+float(vegDowns))
    revScores['local']=float(localUps)/(float(localUps)+float(localDowns))
    for k,v in revScores.items():
        if (v>0.7):
            Badge.objects.create(name=k,restaurant=id)
    revScores['comb'] = (revScores['waste'] + revScores['water'] + revScores['veg'] + revScores['local'])*5.0/4.0
    return revScores

def dist(lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])

    #haversine
    a = sin((lat2-lat1)/2)**2 + cos(lat1) * cos(lat2) * sin((long2-long1)/2)**2
    c = 2*asin(sqrt(a))
    return c*6371

def search(request):
    Review.objects.all().delete()
    lat = request.GET.get('lat', None)
    if lat is None:
        lat = '51.509865'
    long = request.GET.get('lon', None)
    if long is None:
        long = '-0.118092'
    q = request.GET.get('q', '')
    if q is not '':
        q = '&q='+q
    r = requests.get('https://developers.zomato.com/api/v2.1/search?entity_type=zone'+q+'&lat='+lat+'&lon='+long+'&radius=1000&sort=real_distance&order=asc', \
    headers={"Accept": 'application/json', "user-key": '0db40869c4ea2cc5a9c1b27838491559'})
    r = r.json()['restaurants']
    outList = []
    for resto in r:
        new = {}
        inner = resto['restaurant']
        location = inner['location']
        new['id'] = inner['id']
        reviews = Review.objects.filter(restaurant=new['id'])
        if not reviews:
            genReviews(new['id'])
        new['name'] = inner['name']
        revScores = scoreReviews(new['id'])
        new['sustain_rating'] = revScores['comb']
        new['imgUrl'] = inner['featured_image']
        new['locality'] = location['locality_verbose']
        new['cuisines'] = inner['cuisines']
        badges = Badge.objects.filter(restaurant = new['id'])
        print(badges)
        seri = BadgeSerializer(badges, many=True)

        new['badges'] = seri.data
        new['rating'] = inner['user_rating']['aggregate_rating']
        new['dist'] = str(dist(float(lat), float(long), float(location['latitude']), float(location['longitude'])))
        outList.append(new)
    return JsonResponse(outList, safe=False)


class Dummy(APIView):
    queryset = Restaurant.objects.all()
    def get(self, request):
        Restaurant.objects.all().delete()
        Review.objects.all().delete()

        resto = Restaurant.objects.create(name="Joeys Pizza", imgUrl="https://media-cdn.tripadvisor.com/media/photo-s/08/6b/5c/ed/photo0jpg.jpg", address="1 joey road", locality="Joey, Sydney", lat=-33.14, long=151.2321)
        rev = Review.objects.create(restaurant=resto, score="4")
        rev = Review.objects.create(restaurant=resto, score="3")

        resto = Restaurant.objects.create(name="Marios Pizza", imgUrl="https://media-cdn.tripadvisor.com/media/photo-s/08/6b/5c/ed/photo0jpg.jpg", address="1 mario road", locality="Joey, Sydney", lat=-33.14, long=151.2321)
        rev = Review.objects.create(restaurant=resto, score="4")
        rev = Review.objects.create(restaurant=resto, score="5")

        return Response("ok")


class RestaurantList(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        nameSearch = self.request.query_params.get('q', None)
        print(nameSearch)
        if nameSearch is not None:
            queryset = queryset.filter(name__icontains=nameSearch)
        return queryset.annotate(avg_rating=Avg('reviews__score'))
