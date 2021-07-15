from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class deafyPageView(TemplateView):
    template_name = 'for_the_deaf.html'

class blindPageView(TemplateView):
    template_name = 'for_the_blind.html'