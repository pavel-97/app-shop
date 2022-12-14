from django.forms import ModelForm, Textarea, TextInput
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.db.models import F

from app_profile.models import Profile, HistoryOrder

from . import models
from . import tools
from . import decorators


class CommentForm(ModelForm):
    """
    Класс CommentForm. Наследние класса ModelForm.
    Реализует форму создания комментариев.
    """    
    def save(self, request, slug, *args, **kwargs):
        comment = models.ProductComment.objects.create(
            profile=Profile.objects.get(user=request.user),
            product=models.Product.objects.get(slug=slug),
            comment=self.cleaned_data.get('comment')
        )
        return comment

    class Meta:
        model = models.ProductComment
        fields = ('comment', )
        widgets = {
            'comment': Textarea(attrs={'class': 'form-textarea', 'id': 'review', 'placeholder': 'Review'})
        }
        
        
class MakeOrderForm(ModelForm):
    """
    Класс MakeOrderForm. Наследние класса ModelForm.
    Реализует форму создания заказа.
    """
    def take_products_from_storage(self):
        basket = cache.get('basket', dict())
        for product, count in basket.items():
            storage = models.ProductStorage.objects.get(product=product)
            storage.count = F('count') - int(count)
            storage.save()
        return None
    
    def clean_count(self, *args, **kwargs):
        basket = cache.get('basket', dict())
        for product, count in basket.items():
            storage = tools.get_or_error(models.ProductStorage, product)
            if storage.count < int(count):
                raise ValidationError('Too biggest count ({}) for {}.'.format(
                    count,
                    product.title,
                    ))
        self.take_products_from_storage()
        return True
    
    def clean(self, *args, **kwargs):
        self.clean_count(*args, **kwargs)
        return super().clean()
    
    def create_product_order(self):
        basket = cache.get('basket', dict())
        order_set = list()
        for product, count in basket.items():
            order_set.append(models.ProductOrder.objects.create(product=product, count=count))
        order_set = tuple(order_set)
        return order_set
    
    @decorators.include_delivery
    def add_product_order(self, order, set_product_order):
        total_price = 0
        for product_order in set_product_order:
            order.product_order.add(product_order)
            total_price += (product_order.product.price * int(product_order.count))
        order.total_price = total_price
        order.save()
        return order
    
    def add_history_order(self, request, order):
        history_order, _ = HistoryOrder.objects.get_or_create(profile=request.user.profile)
        history_order.orders.add(order)
        return None
    
    @decorators.delete_basket
    def save(self, request, *args, **kwargs):
        set_product_order = self.create_product_order()
        order = models.Order.objects.create(
            profile=request.user.profile,
            delivery=request.POST.get('delivery'),
            pay=request.POST.get('pay'),
            **self.cleaned_data,
        )
        self.add_product_order(order, set_product_order)
        self.add_history_order(request, order)
        return order
        
    class Meta:
        model = models.Order
        fields = ('telephon_number', 'city', 'address', 'comment')
        widgets = {
            'telephon_number': TextInput(attrs={'class':'form-input'}, ),
            'city': TextInput(attrs={'class': 'form-input'}, ),
            'address': Textarea(attrs={'class': 'form-input'}, ),
            'comment': Textarea(attrs={'class': 'form-input'}, )
        }