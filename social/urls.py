from django.urls import path
from . import views

urlpatterns = [
    path('', views.getSocial.as_view()),
]
