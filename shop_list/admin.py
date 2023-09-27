from django.contrib import admin
from .models import Catalog_section, Product, Units
from django.db.models import QuerySet
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_unit', 'counting', 'section', 'name_ru']
    list_editable = ['name_unit', 'counting', 'section', 'name_ru']
    ordering = ['name']
    search_fields = ['name__istartswith', 'section']
   # exclude = ['slug']
    prepopulated_fields = {'slug': ('name',)}

class Catalog_sectionAdmin(admin.ModelAdmin):
    list_display = ['name_section', 'name_ru']
    list_editable = ['name_ru']
    ordering = ['name_section']
    search_fields = ['name__istartswith']
    # exclude = ['slug']
    prepopulated_fields = {'slug': ('name_section',)}


admin.site.register(Catalog_section, Catalog_sectionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Units)