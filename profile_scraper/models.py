# coding=utf8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class Profile(models.Model):
    twitterSource = models.CharField(max_length=100, unique=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    jobTitle = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100, null=True, blank=False)
    cdSize = models.CharField(max_length=40, null=True)
    cdIndustry = models.CharField(max_length=40, null=True)
    hqCity = models.CharField(max_length=20, null=True)
    hqState = models.CharField(max_length=20, null=True)
    hqCountry = models.CharField(max_length=20, null=True)
    twitterUserName = models.CharField(max_length=100, unique=True, default="No Handle Entered: " + str(datetime.now()))
    ngrams = models.CharField(max_length=10, null=True)
    statuses_count = models.IntegerField(default=0)
    influencer = models.BooleanField(default=False)
    followers_count = models.IntegerField(null=True)
    following_count = models.IntegerField(null=True)
    description = models.TextField()
    friends_count = models.IntegerField()
    profile_image_url = models.URLField()

    def __str__(self):
        return self.twitterUserName

class Tweet(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tweetId = models.CharField(max_length=100)
    tweetRawText = models.CharField(max_length=140)
    tweetProcText = models.CharField(max_length=140)
    isBusiness = models.FloatField()

    def __str__(self):
        return self.tweetId

