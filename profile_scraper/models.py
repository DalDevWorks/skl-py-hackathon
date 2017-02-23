from __future__ import unicode_literals

from django.db import models

class Profile(models.Model):
    twitterSource = models.CharField(max_length=100, unique=True)
    handle = models.CharField(max_length=100, unique=True, default="No Handle Entered")
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    influencer = models.CharField(max_length=16)
    followers = models.IntegerField(null=True)
    following = models.IntegerField(null=True)
    description = models.TextField()
    def __str__(self):
        return self.handle
