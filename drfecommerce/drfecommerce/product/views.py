from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from product.models import Category
from product.serializers import CategorySerializer

# Create your views here.
class CategoryView(viewsets.ViewSet):
  """
  Simple ViewSet for viewing categories
  """
  queryset = Category.objects.all()

  def list(self, request):
    serializer = CategorySerializer(self.queryset, many=True)
    return Response(serializer.data)