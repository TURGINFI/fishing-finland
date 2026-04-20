from django.contrib.auth.models import User
from django.db import models


class PlatformMessage(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='platform_messages')
    subject = models.CharField(max_length=200)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message to {self.recipient.username}: {self.subject}"
