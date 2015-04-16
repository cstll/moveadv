from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class AdventureUser(models.Model):
  # Primary key
  user_id_num = models.AutoField(primary_key=True)

  # Underlying django user object - has username, email and password
  django_user = models.ForeignKey(User)

  first_name = models.CharField(max_length=255,null=True, blank=True)
  last_name = models.CharField(max_length=255,null=True, blank=True)

  street_address = models.CharField(max_length=255,null=True, blank=True)
  city = models.CharField(max_length=255,null=True, blank=True)
  state = models.CharField(max_length=255,null=True, blank=True)
  zipcode = models.CharField(max_length=255,null=True, blank=True)
  
  phone = models.CharField(max_length=255,null=True, blank=True)
  
  gender = models.CharField(max_length=255,null=True, blank=True)

  bday_month = models.IntegerField(default=1)
  bday_day = models.IntegerField(default=1) 
  bday_year = models.IntegerField(default=0)

  allergies = models.CharField(max_length=2000,null=True, blank=True)
  found_us = models.CharField(max_length=2000,null=True, blank=True)

  def __str__(self):
    return (self.first_name if self.first_name else "") + " " + (self.last_name if self.last_name else "")

class Instructor(models.Model):
  # Primary key
  instructor_id_num = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255,null=True, blank=True)
  bio = models.CharField(max_length=2000,null=True, blank=True)
  def __str__(self):
    return (self.name if self.name else "New Instructor")

class Trip(models.Model):
  # Primary key
  trip_id_num = models.AutoField(primary_key=True)

  date = models.DateTimeField(default=timezone.now)
  title = models.CharField(max_length=255,null=True, blank=True)
  instructor = models.ForeignKey(Instructor)
  intensity = models.IntegerField(default=0)
  technicality = models.IntegerField(default=0)

  description = models.CharField(max_length=8000,null=True, blank=True)
  description2 = models.CharField(max_length=8000,null=True, blank=True)

  meeting_location = models.CharField(max_length=2000,null=True, blank=True)
  meeting_time = models.DateTimeField(default=timezone.now)
  end_time = models.DateTimeField(default=timezone.now)
  
  things_to_bring = models.CharField(max_length=8000,null=True, blank=True)

  trip_image = models.ImageField(upload_to="images/", blank=True, null=True)   

  price = models.IntegerField(default=109)
  
  minimum_to_go = models.IntegerField(default=10)
  
  def __str__(self):
    return (self.title if self.title else "New Trip")


class UserTrips(models.Model):
  # Primary key
  user_trip_id_num = models.AutoField(primary_key=True)
  
  user = models.ForeignKey(AdventureUser)
  trip = models.ForeignKey(Trip)
  def __str__(self):
    return (self.user.__str__() if self.user.__str__() else "") + " : " + (self.trip.__str__() if self.trip.__str__() else "")
  class Meta:
    managed = True
    verbose_name_plural = 'User Trips'

  
