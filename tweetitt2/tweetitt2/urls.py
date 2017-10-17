"""tweetitt2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import home
from tweet.views import home_tweet, tweet_detail_view, tweet_list_view, TweetListView,  TweetDetailView
from tweet.views import TweetCreateView, TweetUpdateView, TweetDeleteView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^tweet/$', home_tweet, name='home_tweet'),
    url(r'^tweet/detail$', tweet_detail_view, name='tweet_detail'),
    url(r'^tweet/list$', tweet_list_view, name='tweetlist'),
    url(r'^tweet/create$', TweetCreateView.as_view(), name='tweet_create'),
    url(r'^tweet/detail/(?P<pk>\d)/edit/$', TweetUpdateView.as_view(), name='tweet_edit'),
    url(r'^tweet/detail/(?P<pk>\d)/delete/$', TweetDeleteView.as_view(), name='tweet_delete'),
    url(r'^tweet/detail/(?P<id>\d)/$', TweetDetailView.as_view(), name='tweet_detail'),
    url(r'^tweet/listc$', TweetListView.as_view(), name='tweet_list'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
