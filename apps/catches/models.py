from django.contrib.auth.models import User
from django.db import models


class CatchLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='catch_logs')
    fish_name = models.CharField(max_length=120)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    length_cm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    caught_at = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.fish_name} by {self.user.username}"
