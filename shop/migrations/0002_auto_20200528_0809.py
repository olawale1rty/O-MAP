# Generated by Django 3.0 on 2020-05-28 07:09

from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

# DATA_FILENAME = 'data.json'
# def load_data(apps, schema_editor):
#     Shop = apps.get_model('shop', 'Shop')
#     jsonfile = Path(__file__).parents[2] / DATA_FILENAME

#     with open(str(jsonfile), encoding="utf8") as datafile:
#         objects = json.load(datafile)
#         for obj in objects['elements']:
#             try:
#                 objType = obj['type']
#                 if objType == 'node':
#                     tags = obj['tags']
#                     name = tags.get('name','no-name')
#                     longitude = obj.get('lon', 0)
#                     latitude = obj.get('lat', 0)
#                     location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
#                     Shop(name=name, location = location).save()
#             except KeyError:
#                 pass     
#load_data

class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython()
    ]
