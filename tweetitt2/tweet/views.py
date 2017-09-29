# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .forms import TweetModelForm
from .models import Tweet


# Create your views here.

def home_tweet(request):
    print request
    v = "Desde home tweet"
    v2 = {"Usuario":"Christian"}
    return render(request, "home.html", {'v':v, 'v2':v2})

#CRUD Create Retrive or Read Update Delete

class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = "tweets/form.html"
    success_url = "/tweet/listc"

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     print form.instance.user
    #     return super(TweetCreateView, self).form_valid(form)




#With built in django generic Class-based
class TweetDetailView(DetailView):
    template_name = "tweets/tweet_detail.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return Tweet.objects.get(id=id)

    def get_context_data(self, *args, **kwargs):
        context = super(TweetDetailView, self).get_context_data(*args, **kwargs)
        print context
        return context


class TweetListView(ListView):
    template_name = "tweets/tweet_list.html"
    queryset = Tweet.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(TweetListView, self).get_context_data(*args, **kwargs)
    #     print context
    #     return context



# Retrive GET desde la base de datos
def tweet_detail_view(request, id=1):
    # msg = "vista de detalle"
    result_set = Tweet.objects.get(id=id)
    context = {
        "result": result_set
    }
    return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):
    result_set = Tweet.objects.all()
    context = {
        "result": result_set
    }
    return render(request, "tweets/list_view.html", context)
