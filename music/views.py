from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import Song
from .serializers import SongSerializer


class SongListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    queryset = Song.objects.all()
    serializer_class = SongSerializer

