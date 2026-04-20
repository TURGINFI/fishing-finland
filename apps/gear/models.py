from django.db import models


class GearRecommendation(models.Model):
    title = models.CharField(max_length=180)
    category = models.CharField(max_length=120)
    description = models.TextField()
    partner_url = models.URLField()
    image_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
