from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    """Admin View for Image"""

    pass
