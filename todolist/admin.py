from django.contrib import admin

# Register your models here.

from todolist.models import Item
admin.site.register(Item)
