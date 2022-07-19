from django.db import models
from core.models import TimeStampedModel

class Social(TimeStampedModel):
    
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.facebook