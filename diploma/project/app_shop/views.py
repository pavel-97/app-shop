from django.shortcuts import render
from django.views.generic import View, DetailView, ListView
from django.db.models import Min

from . import tools
from . import models
from . import utility

# Create your views here.


class HomeView(ListView):
    template_name = 'app_shop/index.html'
    queryset = models.Product.objects.all().select_related('category').prefetch_related('tag')
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all().annotate(Min('product__price'))[:3]
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(title__icontains=self.request.GET.get('query', ''))
        return queryset


class ProductListView(utility.ProductQuerysetFilterMixin, utility.ProductListOrderByMixin, utility.SearchMixin, ListView):
    model = models.Product
    
    
class ProductListOrderByDateListView(utility.ProductQuerysetFilterMixin, utility.ProductListOrderByMixin, utility.SearchMixin, ListView):
    model = models.Product
    field = '-updated_at'


class ProductListOrderByPriceListView(utility.ProductQuerysetFilterMixin, utility.ProductListOrderByMixin, utility.SearchMixin, ListView):
    model = models.Product
    field = '-price'


class ProductDetailView(DetailView):
    model = models.Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characteristics'] = context.get('product').characteristic.split('\n')
        context['other_characteristics'] = tools.get_dict_characteristics(context.get('product').other_characteristic)
        context['additional_info'] = tools.get_dict_characteristics(context.get('product').additional_info)
        return context
    
    
class BasketView(View):
    def get(self, request):
        return render(request, 'app_shop/basket.html')