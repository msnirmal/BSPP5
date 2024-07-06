from django.contrib import admin
from .models import Product, Category



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',         
        'name',
        'author',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'friendly_name',
    )
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

