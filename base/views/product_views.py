from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.models import Products
from base.products import products
from base.serializer import ProductsSerializer

# Create your views here.

from rest_framework import status


@api_view(['GET'])
def getProducts(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Products.objects.get(id = pk)
    serializer = ProductsSerializer(product, many= False)
    return Response(serializer.data)
