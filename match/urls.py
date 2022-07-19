from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMatches.as_view()),
]
