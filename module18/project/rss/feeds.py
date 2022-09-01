from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from blog.models import News


class LatestNewsFeed(Feed):
    title = _(News.__class__.__name__)
    link = '/sitenews/'
    description = 'Latest news'

    def items(self):
        return News.objects.all().order_by('-publicated_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse_lazy('detail_news', kwargs={'pk': item.pk})
