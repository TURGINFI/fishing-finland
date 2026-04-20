from django.contrib import admin
from .models import FishingSpot

@admin.register(FishingSpot)
class FishingSpotAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'best_season')
