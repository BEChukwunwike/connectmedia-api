"""Followers models."""
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Follower(models.Model):
    """Follower model."""

    owner = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    followed = models.ForeignKey(
        User, related_name="followed", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class."""

        ordering = ["-created_at"]
        unique_together = ["owner", "followed"]

    def __str__(self):
        """Return follower."""
        return f"{self.owner} {self.followed}"
