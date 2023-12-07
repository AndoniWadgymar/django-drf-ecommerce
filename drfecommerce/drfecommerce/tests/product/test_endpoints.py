import pytest
import factory
import json

pytestmark = pytest.mark.django_db

class TestCategoryEndpoints:
  #prepare endpoint
  endpoint = "/api/category/"

  def test_category_get(self, category_factory, api_client):
    #Arrange
    #we create a factory with 4 untis
    category_factory.create_batch(4)
    #Act
    response = api_client().get(self.endpoint)
    #Assert
    assert response.status_code == 200
    print(json.loads(response.content))
    assert len(json.loads(response.content)) == 4


class TestBrandEndpoints:
  endpoint = "/api/brand/"

  def test_brand_get(self, brand_factory, api_client):
    #Arrange
    #we create a factory with 4 untis
    brand_factory.create_batch(2)
    #Act
    response = api_client().get(self.endpoint)
    #Assert
    assert response.status_code == 200
    print(json.loads(response.content))
    assert len(json.loads(response.content)) == 2

class TestProductEndpoints:
  endpoint = "/api/product/"

  def test_product_get(self, product_factory, api_client):
    #Arrange
    #we create a factory with 4 untis
    product_factory.create_batch(2)
    #Act
    response = api_client().get(self.endpoint)
    #Assert
    assert response.status_code == 200
    print(json.loads(response.content))
    assert len(json.loads(response.content)) == 2