from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet

router = DefaultRouter()
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]