from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import New

# Create your views here.



class News(TemplateView):
    template_name = "news/news.html"
    def get_context_data(self, **kwargs):
        context = super(News, self).get_context_data(**kwargs)
        context['news'] = New.objects.order_by('-pub_date').first()
        context['all_news'] = New.objects.order_by('-pub_date')
        return context

def older_news(request, news_id):
    all_news = New.objects.filter(pk=news_id)
    older_news = New.objects.order_by('-pub_date')
    return render(request, 'news/older_news.html', {'all_news': all_news, 'older_news': older_news})
