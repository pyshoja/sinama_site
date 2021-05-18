from django.contrib import admin

# Register your models here.

from .models import Janer, Film, Profile, sans , Location


class janeradmin (admin.ModelAdmin):
    list_display = ('janer_name' , 'janer_tozihat')
    list_filter = ('janer_name' , 'janer_tozihat')
    search_fields = ('janer_name' , 'janer_tozihat')

admin.site.register(Janer , janeradmin)


class filmadmin (admin.ModelAdmin):
    list_display = ('name_film' ,'namber_film' , 'name_janer' , 'karghardan' , 'jalalidatetime')
    list_filter = ('name_film' , 'name_janer' , 'karghardan' , 'time_film')
    search_fields = ('namber_film' , 'name_film' , 'name_janer' , 'karghardan' , 'time_film')

admin.site.register(Film , filmadmin)


class sansadmin (admin.ModelAdmin):
    list_display = ('film_sans' , 'namber_sans' , 'jalalidatetime' , 'local_sans' , 'status_sans')
    list_filter = ('film_sans' , 'time_sans' , 'status_sans')
    search_fields = ('namber_sans' , 'film_sans' , 'time_sans' , 'local_sans' , 'status_sans')

admin.site.register(sans , sansadmin)


class lacationadmin (admin.ModelAdmin):
    list_display = ('name_location' , 'ostan' , 'adress_location' , 'phone_location')
    list_filter = ('name_location' , 'ostan')
    search_fields = ('name_location' , 'ostan' , 'adress_location' , 'phone_location')

admin.site.register(Location , lacationadmin)


class profileadmin (admin.ModelAdmin):
    list_display = ('first_name' , 'last_name' , 'jens' , 'imail_name' , 'phone_name')
    list_filter = ('first_name' , 'last_name' , 'jens' , 'imail_name' , 'phone_name')
    search_fields = ('first_name' , 'last_name' , 'jens' , 'imail_name' , 'phone_name')

admin.site.register(Profile , profileadmin)
