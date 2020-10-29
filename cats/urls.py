from django.urls import path

from cats.views import CatRandomView

urlpatterns = [
    path('random', CatRandomView.as_view(), name="home"),
]