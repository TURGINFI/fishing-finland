from django.contrib import admin
from .models import CatchLog

@admin.register(CatchLog)
class CatchLogAdmin(admin.ModelAdmin):
    list_display = ('fish_name', 'user', 'caught_at', 'location')
