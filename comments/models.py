"""Comments models"""
from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Create your models here.
class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        """Meta class"""
        ordering = ['-created_at']

    def __str__(self):
        """Return comment content"""
        return str(self.content)
