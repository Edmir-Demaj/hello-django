from django.contrib import admin
from .models import Item
# from current directory import class Item

# Register your models here.
admin.site.register(Item)
# register our Item model in admin page
