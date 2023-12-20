"""Posts serializers."""
from rest_framework import serializers
from likes.models import Like
from .models import Post


# Create your serializers here.
class PostSerializer(serializers.ModelSerializer):
    """Post serializer."""

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_picture = serializers.ReadOnlyField(source="owner.profile.picture.url")
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_picture(self, value):
        """Validate picture."""
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image file too large ( > 2mb )")
        if value.image.width > 4096 or value.image.height > 4096:
            raise serializers.ValidationError("Image height or width is too large")
        return value

    def get_is_owner(self, obj):
        """Get is owner."""
        request = self.context["request"]
        return request.user == obj.owner

    def get_like_id(self, obj):
        """Get like id."""
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    class Meta:
        """Meta class."""

        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_picture",
            "created_at",
            "modified_at",
            "title",
            "content",
            "picture",
            "image_filter",
            "like_id",
            "likes_count",
            "comments_count",
        ]
