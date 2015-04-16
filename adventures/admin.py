from django.contrib import admin
from django.contrib.auth.models import User

from adventures.models import *

admin.site.register(Trip)
admin.site.register(Instructor)
admin.site.register(UserTrips)
admin.site.register(AdventureUser)
