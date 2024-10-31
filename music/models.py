from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    img = models.URLField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
