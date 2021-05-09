from django.contrib import admin

# Register your models here.

from .models import Janer, Film, Profile, sans , Location

admin.site.register(Janer)
admin.site.register(Film)
admin.site.register(sans)
admin.site.register(Location)
admin.site.register(Profile)
