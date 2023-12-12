"""Profiles models"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    """Profile model"""
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    picture = models.ImageField(
        upload_to='images/', default='../default_profile_innwhf'
    )

    class Meta:
        """Meta class"""
        ordering = ['-created_at']

        def __str__(self):
            """Return name and username."""
            return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    """Create profile when user is created."""
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
