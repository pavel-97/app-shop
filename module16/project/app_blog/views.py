from time import time

from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.db.models import Count, Min, Max, Avg

from . import models
from . import tools

# Create your views here.


class RecordListView(ListView):
    queryset = models.Record.objects.prefetch_related('blog_set').all().prefetch_related('author').select_related('moderator')


# def test(request):
#     t1 = time()
#     for i in range(1000):
#         models.Record.objects.create(title=tools.gen_date(i))
#     print(time()-t1)
#     return HttpResponse('Hello world')

# def test(request):
#     t1 = time()
#     date = [models.Record(title=tools.gen_date(i)) for i in range(1000)]
#     models.Record.objects.bulk_create(date)
#     print(time()-t1)
#     return HttpResponse('Hello World')

# def test(request):
#     t1 = time()
#     objs = models.Record.objects.filter(title__contains='test').update(title=tools.gen_date(3))
#
#     print(time()-t1)
#     return HttpResponse('Hello world')

# def test(request):
#     t1 = time()
#     objs = models.Record.objects.filter(title__contains='test_title')
#     for i, obj in enumerate(objs):
#         obj.title = tools.gen_date(i)
#     models.Record.objects.bulk_update(objs, ['title'])
#     print(time()-t1)
#     return HttpResponse('Hello World')

def test(request):
    blogs = models.Blog.objects.annotate(Count('record'))
    return render(request, 'app_blog/test.html', {'blogs': blogs})
