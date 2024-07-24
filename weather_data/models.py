# Django management command to create a new app

# models.py
from django.db import models
from django.utils import timezone
import datetime


your_datetime_str = '2024-07-16 13:45'  # Corrected format

# Function to parse the string into a datetime object
def parse_datetime_from_string(datetime_str):
    return timezone.make_aware(datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M'))

class DateTime(models.Model):
    datetime = models.DateTimeField(default=parse_datetime_from_string(your_datetime_str), primary_key=True)
  
class Location(models.Model):
    location = models.CharField(max_length=100, primary_key=True)

class WeatherData(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp_utc = models.ForeignKey(DateTime, on_delete=models.CASCADE)
    temperature = models.FloatField()
    solar_radiation = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.FloatField()
    relative_humidity = models.FloatField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

