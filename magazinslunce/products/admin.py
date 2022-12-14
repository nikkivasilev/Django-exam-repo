from django.contrib import admin

from magazinslunce.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name',)

