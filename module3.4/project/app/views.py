from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def contacts(request):
    context = {
        'phone':  '8-800-708-19-45',
        'email': 'sales@company.com',
    }
    return render(request, 'app/contacts.html', context)


def about(request):
    context = {
        'name': 'бесплатные объявления',
        'text': 'бесплатные объявления в вашем городе!',
    }
    return render(request, 'app/about.html', context)


def categories(request):
    context = {
        'categories': ['личные вещи', 'транспорт', 'хобби', 'отдых'],
    }
    return render(request, 'app/categories.html', context)


def regions(request):
    context = {
        'regions': ['Москва', 'Московская область', 'республика Алтай', 'Вологодская область'],
    }
    return render(request, 'app/regions.html', context)
