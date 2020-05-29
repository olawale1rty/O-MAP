from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop

@admin.register(Shop)
class ShopAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
