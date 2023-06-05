from django.urls import path
from .views import puzzle, home, error
urlpatterns = [
   path("", home, name="home"),
   path("puzzle/", puzzle, name="puzzle"),
   path("error/", error, name="error")
]
