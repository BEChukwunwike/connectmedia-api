"""Tests for the followers app."""
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from .models import Follower
# from .serializers import FollowerSerializer


# Create your tests here.
class FollowerListTestCase(TestCase):
    """Tests for the FollowerList view."""
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_follower(self):
        """Test that a follower can be created."""
        data = {"follower_name": "John Doe"}
        response = self.client.post("/followers/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follower.objects.count(), 1)
        self.assertEqual(Follower.objects.get().follower_name, "John Doe")
        self.assertEqual(Follower.objects.get().owner, self.user)

    def test_list_followers(self):
        """Test that a list of followers can be retrieved."""
        Follower.objects.create(follower_name="John Doe", owner=self.user)
        Follower.objects.create(follower_name="Jane Smith", owner=self.user)

        response = self.client.get("/followers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["follower_name"], "John Doe")
        self.assertEqual(response.data[1]["follower_name"], "Jane Smith")
