from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('register/', views.register, name='register'),
    path('add_post/', views.add_post, name='add-post'),  # Добавьте этот маршрут
]

