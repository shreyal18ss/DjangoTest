from django.db import models
from django.utils import timezone
import datetime


# class ExcelData(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     # Add other fields based on the Excel data you expect

# Assuming your_datetime_str is meant to be a valid datetime string, correct its format first
your_datetime_str = '2024-07-16 13:45'  # Corrected format

# Function to parse the string into a datetime object
def parse_datetime_from_string(datetime_str):
    return timezone.make_aware(datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M'))

   

class ExcelData(models.Model):
    timestamp_utc = models.DateTimeField(default=parse_datetime_from_string(your_datetime_str), primary_key=True)
    temperature = models.FloatField(default=00)
    solar_radiation = models.FloatField(default=00)
    wind_speed = models.FloatField(default=00)
    wind_direction = models.FloatField(default=00)
    relative_humidity = models.FloatField(default=00)
    location = models.TextField(default='Sample')