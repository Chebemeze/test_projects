from django.db import models

# Create your models here.
class Book(models.Model):
  def __str__(self):
    return f"{self.title} by {self.Author}"

  title = models.CharField(max_length=50)
  SNB = models.TextField()
  Author = models.CharField(max_length=50)
  is_available = models.BooleanField(default= True)

class Product(models.Model):
  name = models.CharField(max_length=50)
  description= models.TextField(blank=True)

  price = models.DecimalField(max_digits = 10, decimal_places = 2)
  Discount_price = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True, null = True)

  stock = models.PositiveIntegerField(default=0)
  is_active = models.BooleanField(default=True)

  internal_note = models.TextField(blank=True)

  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.name
