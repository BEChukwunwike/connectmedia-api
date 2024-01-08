"""Followers views."""
from rest_framework import generics, permissions
from followers.models import Follower
from followers.serializers import FollowerSerializer
from connectmedia.permissions import IsOwnerOrReadOnly


# Create your views here.
class FollowerList(generics.ListCreateAPIView):
    """Follower list view."""

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Perform create."""
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """Follower detail view."""

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
