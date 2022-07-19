from django.db import models
from ckeditor.fields import RichTextField
from core.models import TimeStampedModel


class Match(TimeStampedModel):

    tourName = models.CharField(max_length=255)
    teamA = models.CharField(max_length=255)
    teamA_image = models.ImageField(upload_to="media/")
    resultA = models.IntegerField()
    teamB = models.CharField(max_length=255)
    teamB_image = models.ImageField(upload_to="media/")
    resultB = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    stream_url = models.URLField(max_length=200)
    descreption = RichTextField(config_name="awesome_ckeditor", blank=True)

    def __str__(self):
        return f"{self.teamA} vs {self.teamB}"

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
