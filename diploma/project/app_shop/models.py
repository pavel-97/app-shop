from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from time import time
from mptt.models import MPTTModel, TreeForeignKey

from app_profile.models import Profile
from app_profile.validators import phone_number_validator

from . import utility
from . import tools
from . import validators

# Create your models here.


class CategoryMPTT(utility.StrMixin, MPTTModel):
    title = models.CharField(max_length=150, unique=True, verbose_name=_('title'))
    slug = models.SlugField(blank=True, verbose_name=_('slug'))
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image = models.FileField(upload_to=tools.get_path_category, blank=True, null=True, default='app_shop/categories/Electronics_gpKEGby.svg', verbose_name=_('image'))
    
    def save(self, *args, **kwargs):
        self.slug = tools.make_slug(self.title)
        return super().save(*args, **kwargs)
    
    class MPTTMeta:
        order_insertion_by = ('title', )


class Product(utility.StrMixin, models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name=_('title'))
    slug = models.SlugField(max_length=150,verbose_name=_('slug'), blank=True)
    category = models.ForeignKey(CategoryMPTT, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_('category'))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('price'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    images = models.ManyToManyField('ProductImage', related_name='images', blank=True, null=True, verbose_name=_('image(s)'))
    characteristic = models.TextField(blank=True ,verbose_name=_('characteristic'))
    other_characteristic = models.TextField(blank=True ,verbose_name=_('other characteristic'))
    additional_info = models.TextField(blank=True, verbose_name=_('additional info'))
    views = models.PositiveIntegerField(default=0, verbose_name=_('views'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
    is_exist = models.BooleanField(default=True, verbose_name=_('is exist'))
    free_delivery = models.BooleanField(default=False, verbose_name=_('free delivery'))

    def save(self, *args, **kwargs):
        self.slug = tools.make_slug(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('product', kwargs={'slug': self.slug})

    
class ProductImage(utility.StrMixin, models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('product'))
    title = models.CharField(max_length=170, blank=True, unique=True, verbose_name=_('title'))
    image = models.ImageField(upload_to=tools.get_path, verbose_name=_('image'))
    content_image = models.BooleanField(default=False, verbose_name=_('content image'))
    
    def save(self, *args, **kwargs):
        self.title = self.product.title + '_{}'.format(int(time()))
        return super().save(*args, **kwargs)
    
    
class ProductComment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_('profile'))
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_('product'))
    comment = models.TextField(verbose_name=('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    
    def __str__(self):
        return '{} about {}'.format(self.profile.user.username, self.product.title)
    
    
class ProductStorage(models.Model):
    product = models.ForeignKey(Product, unique=True, on_delete=models.SET_NULL, null=True, verbose_name=_('product'))
    count = models.PositiveIntegerField(default=0, verbose_name=_('count'))
    
    def __str__(self):
        return '{}: {}'.format(self.product.title, self.count)
    
    
class Order(models.Model):
    profile = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_('profile'))
    product_order = models.ManyToManyField('ProductOrder', verbose_name=_('product order'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    telephon_number = models.CharField(max_length=12, blank=True, validators=(phone_number_validator, ), verbose_name=_('telephon_number'))
    address = models.CharField(max_length=150, blank=True, verbose_name=_('address'))
    city = models.CharField(max_length=100, blank=True, verbose_name=_('city'))
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name=_('total price'))
    card = models.CharField(max_length=8, blank=True, validators=[validators.validate_card_length, validators.validate_card_even], verbose_name=_('card'))
    comment = models.TextField(blank=True, verbose_name=_('comment'))
    pay = models.CharField(max_length=10, blank=True, null=True, choices=(
        ('ONLINE', 'online'),
        ('SOMEONE', 'someone'),
        ))
    delivery = models.CharField(max_length=10, blank=True, null=True, choices=(
        ('ORDINARY', 'ordinary'),
        ('EXPRESS', 'express'),
        ))
    
    def __str__(self):
        return 'order: {}/id: {}'.format(self.profile, self.pk)
    
    
class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name=_('product'))
    count = models.PositiveIntegerField(default=1, verbose_name=_('count'))
    
    def __str__(self):
        return '{}: {}'.format(self.product.title, self.count)