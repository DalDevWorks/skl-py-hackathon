from django.shortcuts import render
from profile_scraper.twitterQueries import *
from profile_scraper.readCSV import readCSV
from .models import Profile

"""
Index displays form to enter a twitter handle
"""
def index(request):
    #if database is empty, run the csv file through readCSV to create users and populate database
    if(Profile.objects.all().count() == 0):
        readCSV('Corporate-Account-Mapping-GoldSet.csv')
    return render(request, 'profile_scraper/index.html')

"""
Lookup takes a post request from index.html and parses the twitter handle from the form
Uses getProfile() to return a twitter profile object
"""
def lookup(request):
    profile = getProfile(request.POST['twitterUserName'])
    name = profile.name
    return render(request, 'profile_scraper/lookup.html', {'name': name})
