from django.db import models

class Birthdate(models.Model):
  name = models.CharField(max_length=255)
  # You can store the Jalali date as a string if conversion is not needed
  birthdate_jalali = models.CharField(max_length=10, blank=True)
