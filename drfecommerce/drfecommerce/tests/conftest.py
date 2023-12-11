import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import AttributeFactory, AttributeValueFactory, CategoryFactory, BrandFactory, ProductFactory, ProductLineFactory, ProductImageFactory, ProductTypeFactory

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductLineFactory)
register(ProductImageFactory)
register(AttributeFactory)
register(AttributeValueFactory)
register(ProductTypeFactory)

# Used so we dont have to rewrite so many test for our end to end
@pytest.fixture
def api_client():
  return APIClient