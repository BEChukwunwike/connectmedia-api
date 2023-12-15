"""Profiles serializers."""
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Profile model serializer."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class."""
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'modified_at', 'name', 'content', 'picture'
        ]
