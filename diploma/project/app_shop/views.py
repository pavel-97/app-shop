from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import tools
from . import models
from . import utility
from . import decorators
from . import forms

# Create your views here.


class HomeView(utility.CategoryContextMixin, utility.BasketContextMixin, ListView):
    """
    Класс HomeView. Наследник классов CategoryContextMixin, BasketContextMixin, ListView.
    Реализует индексную страницу страницу.
    """
    template_name = 'app_shop/index.html'
    queryset = models.Product.objects.all().select_related('category').prefetch_related('images')
    context_object_name = 'products'
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(title__icontains=self.request.GET.get('query', ''))
        return queryset
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        return context

class ProductListView(
    utility.CategoryContextMixin,
    utility.BasketContextMixin,
    utility.ProductQuerysetFilterMixin,
    utility.SearchMixin,
    utility.ProductListOrderByMixin,
    ListView
    ):
    """
    Класс ProductListView. Наследник классов CategoryContextMixin, BasketContextMixin, ProductQuerysetFilterMixin, SearchMixin, ProductListOrderByMixin, ListView.
    Реализует реализует страницу с товароми.
    """
    model = models.Product
    
    
class ProductListOrderByDateListView(ProductListView):
    """
    Класс ProductListOrderByDateListView. Наследник класса ProductListView.
    Реализует реализует страницу с товароми отсортированным по полю updated_at.
    """
    field = '-updated_at'


class ProductListOrderByPriceListView(ProductListView):
    """
    Класс ProductListOrderByPriceListView. Наследник класса ProductListView.
    Реализует реализует страницу с товароми отсортированным по полю price.
    """
    field = '-price'


class ProductListOrderByViewsListView(ProductListView):
    """
    Класс ProductListOrderByViewsListView. Наследник класса ProductListView.
    Реализует реализует страницу с товароми отсортированным по полю views.
    """
    field = '-views'
    
    
class ProductListOrderByCommentListView(ProductListView):
    """
    Класс ProductListOrderByCommentListView. Наследник класса ProductListView.
    Реализует реализует страницу с товароми отсортированным по полю productcomment__count.
    """
    field = '-productcomment__count'
    
    
class CategoryView(utility.CategoryMixin, ProductListView):
    """
    Класс CategoryView. Наследник класса CategoryMixin, ProductListView.
    Реализует реализует страницу с товароми определенной категории, отсортированным по полю views.
    """
    template_name = 'app_shop/category.html'
    field = '-views'
    

class CategoryOrderByPriceView(CategoryView):
    """
    Класс CategoryOrderByPriceView. Наследник класса CategoryView.
    Реализует реализует страницу с товароми определенной категории, отсортированным по полю price.
    """
    field = '-price'
    
    
class CategoryOrderByDateView(CategoryView):
    """
    Класс CategoryOrderByDateView. Наследник класса CategoryView.
    Реализует реализует страницу с товароми определенной категории, отсортированным по полю updated_at.
    """
    field = '-updated_at'
    
    
class CategoryOrderByCommentView(CategoryView):
    """
    Класс CategoryOrderByCommentView. Наследник класса CategoryView.
    Реализует реализует страницу с товароми определенной категории, отсортированным по полю productcomment__count.
    """
    field = '-productcomment__count'


class ProductDetailView(utility.CategoryContextMixin, utility.BasketContextMixin, DetailView):
    """
    Класс ProductDetailView. Наследник класса CategoryContextMixin, BasketContextMixin, DetailView.
    Реализует реализует страницу с определенным товаром.
    """
    model = models.Product
    form = forms.CommentForm
    context_object_name = 'product'
    
    def get_queryset(self):
        return super().get_queryset().prefetch_related('images')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characteristics'] = context.get('product').characteristic.split('\n')
        context['other_characteristics'] = tools.get_dict_characteristics(context.get('product').other_characteristic)
        context['additional_info'] = tools.get_dict_characteristics(context.get('product').additional_info)
        context['comments'] = context['product'].productcomment_set.select_related('profile__user')
        context['form'] = self.form()
        return context
    
    @decorators.add_review
    @decorators.add_view
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @decorators.permission_denied
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form(request.POST)
        context = dict(form=form) | self.get_context_data()
        if form.is_valid():
            form.save(request, slug=kwargs.get('slug'))
            return redirect(reverse_lazy('product', kwargs={'slug': kwargs.get('slug')}))
        return render(request, 'app_shop/product_detail.html', context)
    
class BasketView(utility.CategoryContextMixin, utility.BasketContextMixin, utility.View):
    """
    Класс BasketView. Наследник класса CategoryContextMixin, BasketContextMixin, View.
    Реализует реализует страницу корзины.
    """
    template_name = 'app_shop/basket.html'
        
    
class AddProductInBasketView(utility.View):
    """
    Класс AddProductInBasketView. Наследник класса View.
    Реализует добавление товара в корзину и перенаправляет на страницу, где был пользователь.
    """
    def get(self, request, slug):
        product = models.Product.objects.prefetch_related('images').get(slug=slug)
        tools.add_product_to_basket(product)
        return redirect(request.META.get('HTTP_REFERER'))
    
    
class DeleteProductFromBasket(utility.View):
    """
    Класс DeleteProductFromBasket. Наследник класса View.
    Реализует удаление товара из корзины.
    """
    def get(self, request, slug):
        product = models.Product.objects.get(slug=slug)
        tools.delete_product_from_basket(product)
        return redirect(reverse_lazy('basket'))
    
    
class MakeOrder(LoginRequiredMixin, utility.CategoryContextMixin, utility.BasketContextMixin, utility.View):
    """
    Класс MakeOrder. Наследник класса LoginRequiredMixin, CategoryContextMixin, BasketContextMixin, View.
    Реализует страницу оформление заказа.
    """
    template_name = 'app_shop/order.html'
    form = forms.MakeOrderForm
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.form(instance=self.request.user.profile)
        return context
    
    @decorators.except_error_with_arg(return_object=redirect, to='basket')
    def get(self, request, *args, **kwargs):
        tools.add_count_product_to_basket(request.GET)
        return super().get(request, *args, **kwargs)
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            order = form.save(request)
            return render(request, 'app_shop/payment.html', self.get_context_data() | {'order': order})
        return render(request, self.template_name, self.get_context_data() | {'form': form})
    
    
class PayOrder(LoginRequiredMixin, utility.CategoryContextMixin, utility.BasketContextMixin, utility.View):
    """
    Класс PayOrder. Наследник класса LoginRequiredMixin, CategoryContextMixin, BasketContextMixin, View.
    Реализует оплату заказа и отображает страницу с ожиданием оплаты.
    """
    template_name = 'app_shop/progress_payment.html'
    
    def post(self, request, order_pk):
        order = models.Order.objects.get(pk=order_pk)
        order.card = request.POST.get('card')
        order.save()
        return render(request, self.template_name, self.get_context_data())