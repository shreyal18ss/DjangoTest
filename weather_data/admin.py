# admin.py (optional)
from django.contrib import admin
from .models import WeatherData, DateTime, Location

admin.site.register(WeatherData)
admin.site.register(DateTime)
admin.site.register(Location)