from django.shortcuts import render
from django.core import serializers
from django.views.generic import DetailView

from . import models

# Create your views here.


def news_list(request):
    news = models.News.objects.all()
    context = {'news_list': news, }
    format = request.GET.get('format')
    if format:
        data = serializers.serialize(format, news)
        context['data'] = data
    return render(request, 'blog/news_list.html', context)


class NewsDetailView(DetailView):
    model = models.News
