from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
#from profile_scraper.getProfile import getProfile
from profile_scraper.twitterQueries import *
from django.urls import reverse

"""
Index displays form to enter a twitter handle
"""
def index(request):
    users = Profile.objects.all()
    return render(request, 'profile_scraper/index.html', {'users' : users})

"""
Lookup takes a post request from index.html and parses the twitter handle from the form
Uses getProfile() to return a twitter profile object
"""
def lookup(request):
    profile = getProfile(request.POST['handle'])
    name = profile.name
    return render(request, 'profile_scraper/lookup.html', {'name': name})
