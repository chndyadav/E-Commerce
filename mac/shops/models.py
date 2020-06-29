from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    public_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="shops/images", default='')

    def __str__(self):
        return self.product_name
