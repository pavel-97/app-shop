from django.urls import path
from . import feeds


urlpatterns = [
    path('latest/feed/', feeds.LatestNewsFeed())
]
