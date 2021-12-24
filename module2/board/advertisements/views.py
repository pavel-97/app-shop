from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_list.html', {})


def advertisement_detail(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_detail.html', {})
