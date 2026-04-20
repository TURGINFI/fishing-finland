from django.contrib import admin
from .models import FishSpecies

@admin.register(FishSpecies)
class FishSpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'latin_name', 'min_size_cm', 'daily_limit')
