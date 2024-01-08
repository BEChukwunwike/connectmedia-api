"""ConnectMedia serializers module."""
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


# Create your serializers here.
class CurrentUserSerializer(serializers.ModelSerializer):
    """Current user serializer."""
    profile_id = serializers.ReadOnlyField(source="profile.id")
    profile_picture = serializers.ReadOnlyField(source="profile.picture.url")

    class Meta(UserDetailsSerializer.Meta):
        """Meta class."""

        fields = UserDetailsSerializer.Meta.fields + ("profile_id", "profile_picture",)
