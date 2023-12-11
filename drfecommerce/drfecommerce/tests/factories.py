import factory

from drfecommerce.product.models import Category, Brand, Product, ProductLine, ProductImage, ProductType, Attribute, AttributeValue, ProductTypeAttribute

class CategoryFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Category

  name = factory.Sequence(lambda n: "Category_%d" % n)

class BrandFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Brand

  name = factory.Sequence(lambda n: "Brand_%d" % n)

class AttributeFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Attribute

  name = "attribute_name_test"
  description = "attribute_description_test"

class ProductTypeFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = ProductType

  name = "test_type"

  #When we have a many to many field we need to use this function tu precreate,
  #it uses the name of the m2m field in the model
  @factory.post_generation
  def attribute(self, create, extracted, **kwargs):
    if not create or not extracted:
      return
    self.attribute.add(*extracted)

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
  product_type = factory.SubFactory(ProductTypeFactory)

class AttributeValueFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = AttributeValue

  attribute_value = "attratibute_test"
  attribute = factory.SubFactory(AttributeFactory)

class ProductLineFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = ProductLine

  price = 10.00
  sku = "123abc"
  stock_qty = 1
  product = factory.SubFactory(ProductFactory)
  is_active = True

  #function to create data in a m2m
  @factory.post_generation
  def attribute_value(self, create, extracted, **kwargs):
    if not create or not extracted:
      return
    self.attribute_value.add(*extracted)

class ProductImageFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = ProductImage

  alternative_text = "test alternative text"
  url = "test.jpg"
  productline = factory.SubFactory(ProductLineFactory)

