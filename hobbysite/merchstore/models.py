from django.db import models

class ProductType(models.Model):
    type_name = models.CharField(max_length=255, default="")
    type_description = models.TextField()

    class Meta:
        ordering = ['type_name']

    def __str__(self):
        return self.type_name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True, related_name="producttype")
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        ordering = ['product_name']

    def __str__(self):
        return self.product_name

