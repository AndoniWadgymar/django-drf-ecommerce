import pytest

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