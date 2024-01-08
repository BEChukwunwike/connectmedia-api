"""Profile views."""
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from connectmedia.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.
class ProfileList(generics.ListAPIView):
    """Profile list view."""

    queryset = Profile.objects.annotate(
        posts_count=Count("owner__post", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "owner__following__followed__profile",
        "owner__followed__owner__profile",
    ]
    ordering_fields = [
        "posts_count",
        "followers_count",
        "follwoing_count",
        "owner__following__created_at",
        "owner__followed__created_at",
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """Profile detail view."""

    queryset = Profile.objects.annotate(
        posts_count=Count("owner__post", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
