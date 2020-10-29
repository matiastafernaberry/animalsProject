from django.views.generic import TemplateView


class DogRandomView(TemplateView):
    template_name = "dog_random.html"


class CatRandomView(TemplateView):
    template_name = "cat_random.html"