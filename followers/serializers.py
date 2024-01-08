"""Followers serializers."""
from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


# Create your serializers here.
class FollowerSerializer(serializers.ModelSerializer):
    """Follower serializer."""

    owner = serializers.ReadOnlyField(source="owner.username")
    followed_name = serializers.ReadOnlyField(source="followed.username")

    class Meta:
        """Meta class."""

        model = Follower
        fields = [
            "id",
            "owner",
            "followed",
            "followed_name",
            "created_at",
        ]

    def create(self, validated_data):
        """Create method."""
        try:
            return super().create(validated_data)
        except IntegrityError as exc:
            raise serializers.ValidationError(
                {"error": "You already followed this user"}
            ) from exc
