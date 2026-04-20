from django.db import models


class FishSpecies(models.Model):
    name = models.CharField(max_length=120)
    latin_name = models.CharField(max_length=120, blank=True)
    min_size_cm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    daily_limit = models.CharField(max_length=120, blank=True)
    methods = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
