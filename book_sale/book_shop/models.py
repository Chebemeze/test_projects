from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

# The following choices belongs to role of the Userprofile class.
# determines the options of the class
CHOICES = [
  ('Admin', 'Admin'),
  ('student', 'Student'),
  ('Lecturer', 'Lecturer'),
]

class Userprofile(models.Model):
  user = models.OneToOneField(User, on_delete= models.CASCADE)
  role = models.CharField(max_length = 100, CHOICES = CHOICES)

# @receiver acts as a signal for autocreating Userprofile whenever a user is created
# create_userprofile is the function that carries out the creation and saving of UserProfile
@receiver(post_save, sender=User)
def create_userprofile(sender, created, instance, **kwargs):
  if created:
    userprofile = Userprofile.objects.create(user=instance)
    if userprofile:
      userprofile.save()