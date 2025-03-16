from django.contrib import admin
from .models import Song


class SongAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "artist", "link", "cover_url"]

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Song, SongAdmin)