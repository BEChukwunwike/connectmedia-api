"""Tests for the comments app."""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Comment


# Create your tests here.
class CommentListTestCase(TestCase):
    """Tests for the CommentList view."""
    def setUp(self):
        """Set up the test client and create a user."""
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.comment = Comment.objects.create(content="Test comment", owner=self.user)
        self.url = reverse("comment-list")

    def test_list_comments(self):
        """Test that a list of comments can be retrieved."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_comment(self):
        """Test that a comment can be created."""
        data = {"content": "New comment"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)
        self.assertEqual(Comment.objects.get(id=2).content, "New comment")


class CommentDetailTestCase(TestCase):
    """Tests for the CommentDetail view."""
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.comment = Comment.objects.create(content="Test comment", owner=self.user)
        self.url = reverse("comment-detail", kwargs={"pk": self.comment.id})

    def test_retrieve_comment(self):
        """Test that a comment can be retrieved."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "Test comment")

    def test_update_comment(self):
        """Test that a comment can be updated."""
        data = {"content": "Updated comment"}
        response = self.client.put(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Comment.objects.get(id=self.comment.id).content, "Updated comment"
        )

    def test_delete_comment(self):
        """Test that a comment can be deleted."""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)
