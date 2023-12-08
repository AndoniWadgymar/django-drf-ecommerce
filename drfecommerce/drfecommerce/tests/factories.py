import factory

from drfecommerce.product.models import Category, Brand, Product, ProductLine

class CategoryFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Category

  name = factory.Sequence(lambda n: "Category_%d" % n)

class BrandFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Brand

  name = factory.Sequence(lambda n: "Brand_%d" % n)

# Since Product has a category and a brand we need to build first these two
class ProductFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Product

  name = factory.Sequence(lambda n: "Product_%d" % n)
  description = "test_description"
  is_digital = True
  brand = factory.SubFactory(BrandFactory)
  category = factory.SubFactory(CategoryFactory)
  is_active = True

class ProductLineFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = ProductLine

  price = 10.00
  sku = "123abc"
  stock_qty = 1
  product = factory.SubFactory(ProductFactory)
  is_active = True