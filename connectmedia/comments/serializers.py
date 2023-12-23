"""Comments serializers."""
from rest_framework import serializers
from .models import Comment


# Create your serializers here.
class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_picture = serializers.ReadOnlyField(source='owner.profile.picture.url')

    def get_is_owner(self, obj):
        """Method to check if the user is the owner of the comment"""
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """Meta class"""
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_picture',
            'post',
            'created_at',
            'modified_at',
            'content',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    """
    post = serializers.ReadOnlyField(source='post.id')
