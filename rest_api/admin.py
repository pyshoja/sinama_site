from django.contrib import admin

# Register your models here.

from .models import testrest


class testadmin (admin.ModelAdmin):
    list_display = ('title','link','writer')
    list_filter = ('title','link','writer')
    search_fields = ('title','link','writer')

admin.site.register(testrest , testadmin)
