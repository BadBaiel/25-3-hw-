from rest_framework import serializers
from .models import Product, Category, Review

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = 'id'.split()

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
