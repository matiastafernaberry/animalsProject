from django.urls import path

from dogs.views import DogRandomView

urlpatterns = [
    path('random', DogRandomView.as_view(), name="home"),
]