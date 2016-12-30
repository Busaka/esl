from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import New

# Create your views here.



class News(TemplateView):
    template_name = "news/news.html"
    def get_context_data(self, **kwargs):
        context = super(News, self).get_context_data(**kwargs)
        try:
            context['news'] = New.objects.get(pk=1)
        except:
            context['news'] = New.objects.all()
        return context
