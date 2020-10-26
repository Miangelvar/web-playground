from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model, TextField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
    #Se crea un usuario

    pass