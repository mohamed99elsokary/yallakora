from django.contrib import admin
from .models import Predict, MatchPredict


class MatchPredictAdmin(admin.ModelAdmin):
    list_display = ("id", "teamA", "teamA_image", "teamB", "teamB_image", "start_date")


admin.site.register(MatchPredict, MatchPredictAdmin)


@admin.register(Predict)
class Admin(admin.ModelAdmin):
    list_display = (
        "id",
        "match",
        "resultA",
        "resultB",
        "who_score_first",
        "name",
        "email",
        "phone",
    )
    list_filter = ("match", "resultA", "resultB")
