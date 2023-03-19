from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', null=True, blank=True)
