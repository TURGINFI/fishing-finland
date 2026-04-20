from django.contrib import admin
from .models import FishingRegulation

@admin.register(FishingRegulation)
class FishingRegulationAdmin(admin.ModelAdmin):
    list_display = ('title', 'area', 'season')
