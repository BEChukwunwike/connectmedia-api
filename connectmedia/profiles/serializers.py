"""Profile serializers."""
from rest_framework import serializers
from followers.models import Follower
from .models import Profile


# Create your serializers here.
class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer."""

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """Get is owner."""
        request = self.context["request"]
        return request.user == obj.owner

    def get_following_id(self, obj):
        """Get following id."""
        user = self.context["request"].user
        if user.is_authenticated:
            following = Follower.objects.filter(owner=user, followed=obj.owner).first()
            return following.id if following else None
        return None

    class Meta:
        """Meta class."""

        model = Profile
        fields = [
            "id",
            "owner",
            "created_at",
            "modified_at",
            "name",
            "content",
            "picture",
            "is_owner",
            "following_id",
            "posts_count",
            "followers_count",
            "following_count",
        ]
