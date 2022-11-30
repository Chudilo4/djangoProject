from django.contrib import admin
from .models import *
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'data_begin', 'data_end', 'slug', 'cat')
    search_fields = ('name', 'data_begin', 'data_end', 'cat')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['list_eq2']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class EquipmentsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CategoryEquipmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'pk')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Events, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Equipments, EquipmentsAdmin)
admin.site.register(CategoryEquipments, CategoryEquipmentsAdmin)
