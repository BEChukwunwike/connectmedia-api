"""Test cases for the posts app."""
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from .views import PostList


class PostListTestCase(TestCase):
    """Test case for the post list view."""
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_post_list(self):
        """Test post list."""
        request = self.factory.get("/posts/")
        request.user = self.user
        view = PostList.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response data

    def test_post_create(self):
        """Test post creation."""
        request = self.factory.post(
            "/posts/", {"title": "Test Post", "content": "Test Content"}
        )
        request.user = self.user
        view = PostList.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 201)
        # Add more assertions to validate the created post
