from django.urls import re_path
from HackApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^weather$',views.weather),
    re_path(r'^stations/([a-zA-Z]+)$',views.stations),
    re_path(r'^buslines$',views.buslines),
    re_path(r'^amenity/([a-zA-Z]+)$',views.amenity),
    #"cafe", "bar", "hospital", "school", "bank","pharmacy", "supermarket", "fast_food", "pub", "cinema", "fuel"
    re_path(r'^test/([0-9]+)$',views.test),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)