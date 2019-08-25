from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('ID','Titulo','Precio')
    