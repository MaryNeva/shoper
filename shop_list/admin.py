from django.contrib import admin
from .models import Catalog_section, Product, Units
from django.db.models import QuerySet
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_unit', 'counting', 'section']
    list_editable = ['name_unit', 'counting', 'section']
    ordering = ['name']
    search_fields = ['name__istartswith']
   # exclude = ['slug']
    prepopulated_fields = {'slug': ('name',)}




admin.site.register(Catalog_section)
admin.site.register(Product, ProductAdmin)
admin.site.register(Units)