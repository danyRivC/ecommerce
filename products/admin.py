from django.contrib import admin
from products.models import Product, ProductImage, ProductCategory, ProductSale


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
class ProductAdmin(admin.ModelAdmin):
    """docstring for ProductAdmin."""
    prepopulated_fields = {"slug":("title",)}
    inlines = [
        ProductImageInLine
    ]
    list_display = ('pk', 'title', 'price','description')
    list_editable = ('title', 'price','description')
    list_filter=(
    'categories',
    )
    search_fields=(
    'title',
    )




admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductSale)
