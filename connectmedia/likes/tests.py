"""Test likes app"""
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from .models import Like
from .serializers import LikeSerializer


class LikeListTestCase(TestCase):
    """LikeList TestCase"""
    self.client = APIClient()
    self.user = User.objects.create_user(
        username="testuser", password="testpassword"
    )
    self.client.force_authenticate(user=self.user)

    def test_like_list(self):
        """Test like list"""
        Like.objects.create(owner=self.user)
        Like.objects.create(owner=self.user)

        response = self.client.get("/likes/")
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_like(self):
        """Test create like"""
        data = {"owner": self.user.id}

        response = self.client.post("/likes/", data)
        like = Like.objects.last()
        serializer = LikeSerializer(like)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(like.owner, self.user)
