"""sustain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from sustainbackendapp import views
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^restaurants/(?P<resto_id>\d+)/comments/$', views.delete_post, name='delete-post'),
    url(r'^api/dummy/$', views.Dummy.as_view()),
    url(r'^api/search/$', views.search),
    url(r'^api/restaurants/$', views.RestaurantList.as_view()),
    re_path('.*', TemplateView.as_view(template_name='index.html')),
]
