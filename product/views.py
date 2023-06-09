from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Review
from rest_framework import status
from .serializers import ProductSerializers, CategorySerializers, ReviewSerializers

@api_view(['GET'])
def categories_list_api_view(request):
    categories = Category.objects.all()
    serializer = CategorySerializers(categories, many=True)
    return  Response(data=serializer.data)


@api_view(['GET'])
def categories_one_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializers(category)
    return Response(data=serializer.data)

@api_view(['GET'])
def product_list_api_view(request):
    product = Product.objects.all()
    serializer = ProductSerializers(product, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def product_one_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializers(product)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_list_api_view(request):
    product = Product.objects.all()
    serializer = ProductSerializers(product, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_one_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializers(review)
    return Response(data=serializer.data)

# @api_view(['GET'])
# def product_detail_api_view(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = ProductSerializers(product)
#     return Response(data=serializer.data)

# @api_view(['GET'])
# def category_one_api_view(request):
#     dict_ = {
#         'title': "Hello World",
#         'description': '',
#         'price': '500',
#         'category': True,
#         'dict': {'key': 'value'}
#     }
#     return Response(data=dict_)




















