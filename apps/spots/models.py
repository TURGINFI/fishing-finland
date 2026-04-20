from django.db import models


class FishingSpot(models.Model):
    name = models.CharField(max_length=180)
    area = models.CharField(max_length=180)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    best_season = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.name
