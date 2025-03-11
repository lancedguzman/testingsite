from django.contrib import admin
from .models import ProductType, Product

class ProductTypeAdmin(admin.ModelAdmin):
    """Creates the ProductType Admin Panel."""
    model = ProductType

    list_display = ('type_name', 'type_description',)
    search_fields = ('type_name',)
    ordering = ('type_name',)


class ProductAdmin(admin.ModelAdmin):
    """Creates the Product Admin Panel."""
    model = Product

    list_display = ('product_name','product_type',
                    'product_description', 'product_price',)
    list_filter = ('product_type',)
    search_fields = ('product_name', 'product_type',)
    ordering = ('product_name',)
    list_editable = ('product_price',)


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
