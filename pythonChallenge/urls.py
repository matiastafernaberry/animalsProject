from django.contrib import admin
from django.urls import include, path

from dogs.views import DogRandomView
from cats.views import CatRandomView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dog/random', DogRandomView.as_view(), name="dogs-random"),
    path('cat/random', CatRandomView.as_view(), name="cats-random"),
]
