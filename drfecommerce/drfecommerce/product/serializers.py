from rest_framework import serializers

from drfecommerce.product.models import Product, Category, Brand, ProductLine

class CategorySerializer(serializers.ModelSerializer):
  #We take the name of the model name and serialize it with another name
  category_name = serializers.CharField(source="name")

  class Meta:
    model = Category
    # Send it with the serializer name
    fields = ["category_name"]

class BrandSerializer(serializers.ModelSerializer):
  class Meta:
    model = Brand
    exclude = ["id"]

class ProductLineSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductLine
    exclude = ["id", "is_active", "product"]

class ProductSerializer(serializers.ModelSerializer):
  brand_name = serializers.CharField(source="brand.name")
  category_name = serializers.CharField(source="category.name")
  product_line = ProductLineSerializer(many=True)

  class Meta:
    model = Product
    fields = ["name", "slug", "description", "brand_name", "category_name", "product_line"]