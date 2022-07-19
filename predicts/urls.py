from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPredicts.as_view()),
    path('add/', views.AddPredict.as_view())
]
