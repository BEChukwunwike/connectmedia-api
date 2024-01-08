"""Test profiles app"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Profile


class ProfileListTestCase(TestCase):
    """ProfileList TestCase"""
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("profile-list")

    def test_profile_list(self):
        """Test profile list"""
        # Create some profiles
        Profile.objects.create(name="John")
        Profile.objects.create(name="Jane")
        Profile.objects.create(name="Alice")

        # Make a GET request to the profile list endpoint
        response = self.client.get(self.url)

        # Assert that the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response contains the correct number of profiles
        self.assertEqual(len(response.data), 3)

        # Assert that the profiles are ordered by created_at in descending order
        profiles = Profile.objects.order_by("-created_at")
        for i, profile in enumerate(profiles):
            self.assertEqual(response.data[i]["name"], profile.name)
