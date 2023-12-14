from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializers
from rest_framework import status

# Create your views here.
class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializers(profiles, many=True)
        return Response(serializer.data)
    

class ProfileDetail(APIView):
    serializer_class = ProfileSerializers
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializers(profile)
        return Response(serializer.data)
    
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializers(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete the object by its primary key (id).
    
    def delete(self, request, pk):
        profile = self.get_object(pk)
        profile.delete()
        return Response({"message":"Successfully deleted!"},status=200)
    