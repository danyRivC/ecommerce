from django.contrib import admin
from products.models import Product, ProductImage, ProductCategory

@admin.register(Product,ProductCategory,ProductImage)
class ProductImageInLine(admin.ModelAdmin):
    """docstring for ProductImageInLine."""
    model = ProductImage
class ProductAdmin(admin.ModelAdmin):
    """docstring for ProductAdmin."""
    prepopulated_fields = {"slug":("title",)}
    inlines = [
        ProductImageInLine
    ]
    list_display = ('pk', 'title', 'price')
    list_editable = ('title', 'price')
