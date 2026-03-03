from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Userprofile

# @receiver acts as a signal for autocreating Userprofile whenever a user is created
# create_userprofile is the function that carries out the creation and saving of UserProfile
@receiver(post_save, sender=User)
def create_userprofile(sender, created, instance, **kwargs):
  if created:
    userprofile = Userprofile.objects.create(user=instance)
    if userprofile:
      userprofile.save()