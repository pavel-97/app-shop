from django.shortcuts import render
from django.views.generic import View, DetailView
from django.db.models import Min

from . import tools
from . import models

# Create your views here.


def index(request):
    return render(request, 'app_shop/index.html', {})


class HomeView(View):
    def get(self, request):
        categories = models.Category.objects.all().annotate(Min('product__price'))[:3]
        products = models.Product.objects.all().select_related('category').prefetch_related('tag')
        return render(request, 'app_shop/index.html', {'categories': categories, 'products': products})


class ProductDetailView(DetailView):
    model = models.Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characteristics'] = context.get('product').characteristic.split('\n')
        context['other_characteristics'] = tools.get_dict_characteristics(context.get('product').other_characteristic)
        context['additional_info'] = tools.get_dict_characteristics(context.get('product').additional_info)
        return context