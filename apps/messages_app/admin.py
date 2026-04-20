from django.contrib import admin
from .models import PlatformMessage

@admin.register(PlatformMessage)
class PlatformMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'recipient', 'is_read', 'created_at')
    list_filter = ('is_read',)
