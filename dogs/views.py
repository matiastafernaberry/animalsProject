from django.views.generic import TemplateView


class DogRandomView(TemplateView):
    template_name = "dog_random.html"
