from django.db import models


class FishingRegulation(models.Model):
    title = models.CharField(max_length=200)
    area = models.CharField(max_length=180, blank=True)
    season = models.CharField(max_length=180, blank=True)
    summary = models.CharField(max_length=255, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title
