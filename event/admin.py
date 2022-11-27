from django.contrib import admin
from .models import *
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'data_begin', 'data_end', 'slug', 'cat')
    search_fields = ('name', 'data_begin', 'data_end', 'cat')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Events, EventAdmin)
admin.site.register(Category, CategoryAdmin)
