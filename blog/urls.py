from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPosts.as_view()),
    path('<int:pk>/', views.getPost.as_view()),
]
