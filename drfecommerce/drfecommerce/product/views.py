from django.db import connection

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format

from drf_spectacular.utils import extend_schema

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

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
  # queryset = Product.objects.all()
  # With our custom manager
  queryset = Product.objects.all().isactive()
  lookup_field = "slug"

  def retrieve(self, request, slug=None):
    serializer = ProductSerializer(self.queryset.filter(slug=slug).select_related("category"), many=True)
    data = Response(serializer.data)

    q = list(connection.queries)
    print(len(q))
    print(q)

    return data

  @extend_schema(responses=ProductSerializer)
  def list(self, request):
    serializer = ProductSerializer(self.queryset, many=True)
    return Response(serializer.data)

  @action(methods=["get"], detail=False, url_path=r"category/(?P<category>\w+)/all", url_name="all")
  def list_product_by_Category(self, request, category=None):
    """
    An endpoint to return products by category
    """
    serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
    return Response(serializer.data)

