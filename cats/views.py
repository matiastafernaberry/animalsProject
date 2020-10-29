from django.views.generic import TemplateView


class CatRandomView(TemplateView):
    template_name = "cat_random.html"