# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        # Tweet.objects.create(
        #     user= User.objects.first(),
        #     content = "Some random content"
        # )
        some_random_user = User.objects.create(username="Chrisss")

    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user= User.objects.first(),
            content= "Some random content"
        )
        self.assertTrue(obj.content == "Some random content")
        self.assertTrue(obj.id == 1)
