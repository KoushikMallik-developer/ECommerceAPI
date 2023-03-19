from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


# Create your views here.

@api_view(('GET',))
def get_all_products(request):
    if request.method == "GET":
        all_products = Product.objects.all()
        all_products_serialized = ProductSerializer(all_products, many=True)
        return Response(all_products_serialized.data)

# @api_view(('POST',))
# def create_product(request):
#     if request.method == "POST":
#         products_serialized = ProductSerializer(data=request.data)
#         if products_serialized.is_valid():
#             products_serialized.save()
#         return get_all_products()