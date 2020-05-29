from django.contrib import admin
from .models import Incidence, Country
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class IncidenceAdmin(LeafletGeoAdmin):
	list_display = ('name', 'location')

class CountryAdmin(LeafletGeoAdmin):
	list_display = ('counties', 'codes')

admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(Country, CountryAdmin)
