"""Posts serializers."""
from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Post model serializer."""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_picture = serializers.ReadOnlyField(source='owner.profile.picture.url')

    def validate_picture(self, value):
        """Validate picture"""
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidateError(
                "Image file is too large ( > 2mb)"
            )
        if value.image.width > 4096 or value.image.height > 4096:
            raise serializers.ValidateError(
                "Image height or width is too large"
            )
        return value

    def get_is_owner(self, obj):
        """Check if the user is the owner."""
        request = self.context.get('request')
        return request.user == obj.owner

    class Meta:
        """Meta class."""
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_picture',
            'created_at',
            'modified_at',
            'title',
            'content',
            'picture',
            'image_filter',
        ]