from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import Movie,Theater,Showtime

admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(Showtime)