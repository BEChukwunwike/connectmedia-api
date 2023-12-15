"""ConnectMedia Views"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from connectmedia.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.
class ProfileList(APIView):
    """List all profiles or create a new profile."""
    def get(self, request):
        """Get all profiles."""
        profiles = Profile.objects.all()
        serializer = ProfileSerializers(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    """Retrieve, update or delete a profile instance."""
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        """Get a profile object."""
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """Get a profile."""
        profile = self.get_object(pk)
        serializer = ProfileSerializers(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update a profile."""
        profile = self.get_object(pk)
        serializer = ProfileSerializers(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete the object by its primary key (id).

    def delete(self, request, pk):
        """Delete a profile."""
        profile = self.get_object(pk)
        profile.delete()
        return Response({"message": "Successfully deleted!"}, status=200)
