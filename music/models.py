from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    link = models.URLField()
    cover_url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    def __str__(self):
        return self.title



