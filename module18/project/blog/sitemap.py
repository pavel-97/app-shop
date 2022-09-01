from django.contrib.sitemaps import Sitemap

from . import models


class NewsSitemap(Sitemap):
    changerfreq = 'weekly'
    priority = 0.9

    def items(self):
        return models.News.objects.all()

    def lastmod(self, obj):
        return obj.publicated_at
