"""Likes views."""
from rest_framework import generics, permissions
from likes.models import Like
from likes.serializers import LikeSerializer
from connectmedia.permissions import IsOwnerOrReadOnly


# Create your views here.
class LikeList(generics.ListCreateAPIView):
    """Like list view."""

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Perform create."""
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    """Like detail view."""

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
