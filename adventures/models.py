from django.db import models

class AdventureUser(models.Model):
  # Primary key
  user_id_num = models.AutoField(primary_key=True)

  # Underlying django user object - has username, email and password
  django_user = models.ForeignKey(settings.AUTH_USER_MODEL)

  first_name = models.CharField(max_length=255,null=True, blank=True)
  last_name = models.CharField(max_length=255,null=True, blank=True)

  street_address = models.CharField(max_length=255,null=True, blank=True)
  city = models.CharField(max_length=255,null=True, blank=True)
  state = models.CharField(max_length=255,null=True, blank=True)
  zipcode = models.CharField(max_length=255,null=True, blank=True)
  
  phone = models.CharField(max_length=255,null=True, blank=True)
  
  bday_month = models.IntegerField(default=1)
  bday_day = models.IntegerField(default=1) 
  bday_year = models.IntegerField(default=0)

  allergies = models.CharField(max_length=2000,null=True, blank=True)
  found_us = models.CharField(max_length=2000,null=True, blank=True)
 
class Trip(models.Model):
  # Primary key
  trip_id_num = models.AutoField(primary_key=True)

  date = models.DateTimeField(default=timezone.now)

class UserTrips(models.Model):
  # Primary key
  user_trip_id_num = models.AutoField(primary_key=True)
  
  user = models.ForeignKey(AdventureUser)
  trip = models.ForeignKey(Trip)
  