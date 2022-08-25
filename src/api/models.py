from django.db import models
from datetime import datetime


#  Модель Автора
class Author(models.Model):
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=60, null=False)
    email = models.EmailField(null=False)


#  Модель Продукта
class Product(models.Model):
    name_product = models.CharField(max_length=60, null=False)
    price_product = models.FloatField(null=False)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_product = models.DateField(null=False, default=datetime.now)


#  Модель Фото
class Image(models.Model):
    product_id = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photo_product/")
