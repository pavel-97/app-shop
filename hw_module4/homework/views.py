from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.


class AdvertisementListView(ListView):
    model = models.Advertisement
    context_object_name = 'advertisement_list'


class AdvertisementDetailView(DetailView):
    model = models.Advertisement
