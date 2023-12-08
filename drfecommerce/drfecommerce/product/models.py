from django.db import models
from django.db.models.query import QuerySet
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
#Costum manager changed to this manager
class ActiveManager(models.Manager):
  # def get_queryset(self) -> QuerySet:
  #   return super().get_queryset().filter(is_active=True)
  def isactive(self) -> QuerySet:
    return super().get_queryset().filter(is_active=True)

#We can do the same but with a Queryset
class ActiveQueryset(models.QuerySet):
  def isactive(self) -> QuerySet:
    return self.filter(is_active=True)



class Category(MPTTModel):
  name = models.CharField(max_length=100, unique=True)
  parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
  is_active = models.BooleanField(default=False)
  objects = ActiveQueryset.as_manager()

  class MTTPMeta:
    order_insertion_by = ["name"]

  def __str__(self) -> str:
    return self.name

class Brand(models.Model):
  name = models.CharField(max_length=100, unique=True)
  is_active = models.BooleanField(default=False)
  objects = ActiveQueryset.as_manager()

  def __str__(self) -> str:
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField(max_length=255)
  description = models.TextField(blank=True)
  is_digital = models.BooleanField(default=False)
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
  category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
  is_active = models.BooleanField(default=False)

  #access to the custom manager in Products
  # objects = ActiveManager()
  objects = ActiveQueryset.as_manager()
  # isactive = ActiveManager()

  def __str__(self) -> str:
    return self.name

class ProductLine(models.Model):
  price = models.DecimalField(decimal_places=2, max_digits=5)
  sku = models.CharField(max_length=100)
  stock_qty = models.IntegerField()
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_line")
  is_active = models.BooleanField(default=False)
  objects = ActiveQueryset.as_manager()


