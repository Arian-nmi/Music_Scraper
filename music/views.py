from rest_framework import viewsets
from django.core.cache import cache
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer


class SongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    # Cache playlists for one hour
    def list(self, request, *args, **kwargs):
        category = request.query_params.get('category')
        cache_key = f'songs_{category}' if category else 'songs_all'

        # getting data from cache
        data = cache.get(cache_key)

        if not data:
            queryset = self.queryset
            if category:
                queryset = queryset.filter(category=category)

            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            cache.set(cache_key, data, timeout=60 * 60)

        return Response(data)


    # Endpoint for specific song details
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        song = self.get_object()
        serializer = self.get_serializer(song)
        return Response(serializer.data)
