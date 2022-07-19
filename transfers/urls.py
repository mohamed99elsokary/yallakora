from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTransfers.as_view()),
]
