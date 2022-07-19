from django.db import models
from core.models import TimeStampedModel


class WhoScoreFirst(models.TextChoices):
    """
    WhoScoreFirst
    """

    TEAM_A = "TeamA", "TeamA"
    TEAM_B = "TeamB", "TeamB"
    NO_TEAM = "NoTeam", "NoTeam"


class MatchPredict(TimeStampedModel):
    teamA = models.CharField(max_length=255)
    teamA_image = models.ImageField(upload_to="media/")
    teamB = models.CharField(max_length=255)
    teamB_image = models.ImageField(upload_to="media/")
    start_date = models.DateTimeField()

    def __str__(self):
        return f"{self.teamA} vs {self.teamB}"


class Predict(TimeStampedModel):
    match = models.ForeignKey(MatchPredict, on_delete=models.CASCADE)
    resultA = models.IntegerField()
    resultB = models.IntegerField()
    who_score_first = models.CharField(
        max_length=255, choices=WhoScoreFirst.choices, default=WhoScoreFirst.NO_TEAM
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.email} {self.phone}"
