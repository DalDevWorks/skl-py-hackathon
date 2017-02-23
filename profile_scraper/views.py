from django.shortcuts import render
from profile_scraper.twitterQueries import *
from profile_scraper.readCSV import readCSV
from profile_scraper.businessTweetAlgorithm import determineTweetBusinessWeight
from .models import Profile

"""
Index displays form to enter a twitter handle
"""
def index(request):
    if (Profile.objects.all().count() == 0):
        readCSV('Corporate-Account-Mapping-GoldSet.csv')
    users = Profile.objects.all()
    return render(request, 'profile_scraper/index.html', {'users' : users})

"""
Lookup takes a post request from index.html and parses the twitter handle from the form
Uses getProfile() to return a twitter profile object
"""
def lookup(request):
    twitterUserName = request.POST['twitterUserName']
    if(twitterUserName[0] == '@'):
        twitterUserName = twitterUserName[1:]
    profile = getProfile(twitterUserName)
    # tweets = determineTweetBusinessWeight(twitterUserName)
    return render(request, 'profile_scraper/lookup.html',
        {'profile' : profile,
         #'tweets': tweets
         })