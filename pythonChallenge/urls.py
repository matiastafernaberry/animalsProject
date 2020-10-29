from django.contrib import admin
from django.urls import include, path

from animalsProject.views import DogRandomView, CatRandomView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dog/random', DogRandomView.as_view(), name="home"),
    path('cat/random', CatRandomView.as_view(), name="home"),
]
