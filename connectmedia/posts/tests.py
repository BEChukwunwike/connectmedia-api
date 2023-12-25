"""Test module for posts app."""
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post


# Create your tests here.
class PostListViewTests(APITestCase):
    """Post list view tests."""

    def setUp(self):
        User.objects.create_user(username="Blessing", password="pass")

    def test_can_list_posts(self):
        """Test can list posts."""
        Blessing = User.objects.get(username="Blessing")
        Post.objects.create(owner=Blessing, title="a title")
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        """Test logged in user can create post."""
        self.client.login(username="Blessing", password="pass")
        response = self.client.post("/posts/", {"title": "a title"})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        """Test user not logged in can't create post."""
        response = self.client.post("/posts/", {"title": "a title"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_not_logged_in_cant_list_posts(self):
        """Test user not logged in can't list posts."""
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_user_not_logged_in_cant_update_post(self):
        """Test user not logged in can't update post."""
        Blessing = User.objects.get(username="Blessing")
        Post.objects.create(owner=Blessing, title="a title")
        response = self.client.put("/posts/1/", {"title": "a new title"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_not_logged_in_cant_delete_post(self):
        """Test user not logged in can't delete post."""
        Blessing = User.objects.get(username="Blessing")
        Post.objects.create(owner=Blessing, title="a title")
        response = self.client.delete("/posts/1/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_not_owner_cant_update_post(self):
        """Test user not owner can't update post."""
        Blessing = User.objects.get(username="Blessing")
        Post.objects.create(owner=Blessing, title="a title")
        self.client.login(username="Blessing", password="pass")
        response = self.client.put("/posts/1/", {"title": "a new title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "a new title")

    def test_user_not_owner_cant_delete_post(self):
        """Test user not owner can't delete post."""
        Blessing = User.objects.get(username="Blessing")
        Post.objects.create(owner=Blessing, title="a title")
        self.client.login(username="Blessing", password="pass")
        response = self.client.delete("/posts/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        count = Post.objects.count()
        self.assertEqual(count, 0)
