from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class OurServices(generic.TemplateView):
    template_name = "services.html"
