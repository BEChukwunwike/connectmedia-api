from rest_framework import serializers
from .models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    
    def get_is_owner(self, obj):
        """Get is owner."""
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'modified_at', 'name', 'content', 'picture', 'is_owner'
        ]