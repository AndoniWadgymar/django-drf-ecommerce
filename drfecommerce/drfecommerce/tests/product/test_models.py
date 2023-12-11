import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


class TestCategoryModel:
  def test_str_method(self, category_factory):
    # Arrange
    #We get the data from the conftest thats a file thats first run by pytest and then it creates
    # a test database with the factories.py
    # Act
    obj = category_factory(name="test_category")
    # Assert
    assert obj.__str__() == "test_category"

class TestBrandModel:
  def test_str_method(self, brand_factory):
    # Act
    obj = brand_factory(name="test_category")
    # Assert
    assert obj.__str__() == "test_category"

class TestProductModel:
  def test_str_method(self, product_factory):
    # Act
    obj = product_factory(name="test_product")
    # Assert
    assert obj.__str__() == "test_product"

class TestProductLineModel:
  def test_str_method(self, product_line_factory, attribute_value_factory):
    # Act
    #Many to many class created and then passed to the obj
    attr = attribute_value_factory(attribute_value="test")
    obj = product_line_factory.create(sku="123abc", attribute_value=(attr,))
    # Assert
    assert obj.__str__() == "123abc"

  def test_duplicate_order_value(self, product_line_factory, product_factory):
    obj = product_factory()
    product_line_factory(order=1, product=obj)
    with pytest.raises(ValidationError):
          product_line_factory(order=1, product=obj).clean()

class TestProductTypeModel:
   def test_str_method(self, product_type_factory, attribute_factory):
    # Act
    #Many to many class created and then passed to the obj
    test = attribute_factory(name="test")
    obj = product_type_factory.create(name="test_type", attribute=(test,))
    # Assert
    assert obj.__str__() == "test_type"

class TestAttributeModel:
  def test_str_method(self, attribute_factory):
    # Act
    obj = attribute_factory(name="test_attribute")
    # Assert
    assert obj.__str__() == "test_attribute"

class TestAttributeValueModel:
  def test_str_method(self, attribute_value_factory, attribute_factory):
    # Act
    obj_a= attribute_factory(name="test_attribute")
    obj_b= attribute_value_factory(attribute_value="test_value", attribute=obj_a)
    # Assert
    assert obj_b.__str__() == "test_attribute-test_value"

class TestProductImageModel:
   def test_str_method(self, product_image_factory):
    # Act
    obj = product_image_factory(url="test.jpg")
    # Assert
    assert obj.__str__() == "test.jpg"