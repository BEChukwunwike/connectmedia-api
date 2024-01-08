"""Likes models."""
from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Create your models here.
class Like(models.Model):
    """Like model."""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class."""

        ordering = ["-created_at"]
        unique_together = ["owner", "post"]

    def __str__(self):
        """Return like."""
        return f"{self.owner} {self.post}"
