from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from profile_scraper.getProfile import getProfile
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'profile_scraper/index.html')

def lookup(request):
    twitter = getProfile(request.POST['handle'])
    name = twitter.profile.name
    return render(request, 'profile_scraper/lookup.html', {'name': name})

def display(request, name):
    return render(request, 'profile_scraper/display.html', {'name':name})