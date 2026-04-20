from django.contrib import admin
from .models import FishingGoal

@admin.register(FishingGoal)
class FishingGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'year', 'target_fish', 'target_count', 'progress', 'is_completed')
