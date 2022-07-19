from django.contrib import admin
from . import models
from django.forms import widgets


@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    """Admin View for Match"""
    list_display = (
        "id",
        "tourName",
        "teamA",
        "teamA_image",
        "resultA",
        "teamB",
        "teamB_image",
        "resultB",
        "start_date",
        "end_date",
        "stream_url",
    )
