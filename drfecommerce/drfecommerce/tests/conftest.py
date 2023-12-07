import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import CategoryFactory, BrandFactory, ProductFactory

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)

# Used so we dont have to rewrite so many test for our end to end
@pytest.fixture
def api_client():
  return APIClient