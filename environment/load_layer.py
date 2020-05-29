import os
from django.contrib.gis.utils import LayerMapping
from .models import Country
Country_mapping = {
	'counties': 'Counties',
	'codes': 'Codes',
	'cty_code': 'Cty_CODE',
	'dis': 'dis',
	'geom': 'MULTIPOLYGON',
}

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/counties.shp'))

def load(verbose=True):
	ls = LayerMapping(Country, county_shp, Country_mapping, transform=False, encoding='utf-8')
	ls.save(strict=True,verbose=True)