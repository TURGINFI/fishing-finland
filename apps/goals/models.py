from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class FishingGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fishing_goals')
    year = models.PositiveIntegerField(default=timezone.now().year)
    target_fish = models.CharField(max_length=120)
    target_count = models.PositiveIntegerField(default=1)
    progress = models.PositiveIntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.is_completed = self.progress >= self.target_count
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}: {self.target_fish} ({self.year})"
