from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """Post model."""
    image_filter_choices = [
        ('_2023', '2023'),
        ('jpsconnect', 'Japan'),
        ('indconnect', 'India'),
        ('grcconnect', 'Greece'),
        ('thnconnect', 'Thailand'),
        ('turkconnect', 'Turkey'),
        ('usaconnect', 'USA'),
        ('mexconnect', 'Mexico'),
        ('itaconnect', 'Italy'),
        ('9jaconnect', 'Nigeria'),
        ('chnconnect', 'China'),
        ('franceconnect', 'France'),
        ('spnconnect', 'Spanish'),
        ('brconnect', 'Brazil'),
        ('rusconnect', 'Russia'),
        ('canconnect', 'Canada'),
        ('ausconnect', 'Australia'),
        ('indonconnect', 'Indonesia'),
        ('gerconnect', 'Germany'),
        ('ukconnect', 'UK'),
        ('kconnect', 'Korea'),
        ('saconnect', 'South Africa'),
        ('uaeconnect', 'UAE'),
        ('egconnect', 'Egypt'),
    ]

     # Sort the list alphabetically by the second item in the tuple
    image_filter_choices.sort(key=lambda x: x[1])

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    picture = models.ImageField(
        upload_to="images/", default="../default_post_zuk6nv", blank=True
    )
    image_filter = models.CharField(
        max_length=100, choices=image_filter_choices, default='_2023'
    )

    class Meta:
        """Meta class."""
        ordering = ["-created_at"]

    def __str__(self):
        """Return name and username."""
        return f"{self.id} {self.title}"