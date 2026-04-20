from django.contrib import admin
from .models import GearRecommendation

@admin.register(GearRecommendation)
class GearRecommendationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured')
