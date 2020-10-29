from django.urls import path

from animalsProject.views import DogRandomView, CatRandomView

urlpatterns = [
    path('dog/random', DogRandomView.as_view(), name="home"),
    path('cat/random', CatRandomView.as_view(), name="home"),
]