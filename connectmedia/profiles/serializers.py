"""Profiles serializers."""
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Profile model serializer."""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """Check if the user is the owner."""
        request = self.context.get('request')
        return obj.owner == request.user

    class Meta:
        """Meta class."""
        model = Profile
        fields = [
            'id',
            'owner',
            'created_at',
            'modified_at',
            'name',
            'content',
            'picture',
            'is_owner',
        ]
