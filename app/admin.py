from dataclasses import field
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Editing', {'fields': (('title', 'description'), ('price', 'image'), 'cat', 'available')}),
    )
    list_display = ('__str__', 'cat', 'image', 'available')
    list_editable = ('cat', 'available')
    ordering = ('id',)
    list_filter = ('cat', 'available')
    search_fields = ('id', 'title')

admin.site.register(Carousels)
admin.site.register(categories)
admin.site.register(delivery)
admin.site.register(About)
