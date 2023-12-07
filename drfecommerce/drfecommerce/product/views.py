from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from drfecommerce.product.models import Category, Brand, Product
from drfecommerce.product.serializers import CategorySerializer, BrandSerializer, ProductSerializer

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
  """
  Simple ViewSet for viewing all categories
  """
  queryset = Category.objects.all()

  @extend_schema(responses=CategorySerializer)
  def list(self, request):
    serializer = CategorySerializer(self.queryset, many=True)
    return Response(serializer.data)

class BrandViewSet(viewsets.ViewSet):
  """
  Simple ViewSet for viewing all brands
  """
  queryset = Brand.objects.all()

  @extend_schema(responses=BrandSerializer)
  def list(self, request):
    serializer = BrandSerializer(self.queryset, many=True)
    return Response(serializer.data)

class ProductViewSet(viewsets.ViewSet):
  """
  Simple ViewSet for viewing all products
  """
  queryset = Product.objects.all()

  @extend_schema(responses=ProductSerializer)
  def list(self, request):
    serializer = ProductSerializer(self.queryset, many=True)
    return Response(serializer.data)