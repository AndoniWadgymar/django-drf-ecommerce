from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from drfecommerce.product.models import Category
from drfecommerce.product.serializers import CategorySerializer

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
  """
  Simple ViewSet for viewing categories
  """
  queryset = Category.objects.all()

  @extend_schema(responses=CategorySerializer)
  def list(self, request):
    serializer = CategorySerializer(self.queryset, many=True)
    return Response(serializer.data)