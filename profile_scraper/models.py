from __future__ import unicode_literals

from django.db import models

class UserProfile(models.Model):
	twitterSource = models.CharField(max_length=100, unique=True)
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
	followers = models.IntegerField()
	following = models.IntegerField()
	description = models.TextField()
	def __str__(self):
		return self.handle


# Create your models here.
