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
  def test_str_method(self, product_line_factory):
    # Act
    obj = product_line_factory(sku="123abc")
    # Assert
    assert obj.__str__() == "123abc"

  def test_duplicate_order_value(self, product_line_factory, product_factory):
    obj = product_factory()
    product_line_factory(order=1, product=obj)
    with pytest.raises(ValidationError):
          product_line_factory(order=1, product=obj).clean()
