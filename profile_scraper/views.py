from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
#from profile_scraper.getProfile import getProfile
from profile_scraper.getTwitterProfile import getProfile
from django.urls import reverse

"""
Index displays form to enter a twitter handle
"""
def index(request):
    return render(request, 'profile_scraper/index.html')

"""
Lookup takes a post request from index.html and parses the twitter handle from the form
Uses getProfile() to return a twitter profile object
"""
def lookup(request):
    profile = getProfile(request.POST['handle'])
    name = profile.name
    return render(request, 'profile_scraper/lookup.html', {'name': name})
