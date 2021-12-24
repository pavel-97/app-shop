from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from . import models
from . import forms

# Create your views here.


class AdvertisementListView(ListView):
    model = models.Advertisement
    context_object_name = 'advertisement_list'


class AdvertisementDetailView(DetailView):
    model = models.Advertisement


class AdvertisementFormView(View):
    def get(self,request):
        advertisement_form = forms.AdvertisementForm()
        return render(request, 'homework/advertisement_form.html', {'advertisement_form': advertisement_form, })

    def post(self, request):
        print('post')
        advertisement_form = forms.AdvertisementForm(request.POST)

        if advertisement_form.is_valid():
            models.Advertisement.objects.create(**advertisement_form.cleaned_data)
            return HttpResponseRedirect('advertisements/')

        return render(request, 'homework/advertisement_form.html', {'advertisement_form': advertisement_form, })