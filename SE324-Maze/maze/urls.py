from django.urls import path
from .views import home, maze
urlpatterns = [
    path("", home, name='homeURL'),
    path("maze/", maze, name='mazeURL'),
]
