# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home_tweet(request):
    print request
    v = "Desde home tweet"
    v2 = {"Usuario":"Christian"}
    return render(request, "home.html", {'v':v, 'v2':v2})
