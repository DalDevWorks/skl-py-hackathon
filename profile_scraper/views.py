from django.shortcuts import render
from profile_scraper.addUsers import addUsers
from profile_scraper.businessTweetAlgorithm import determineTweetBusinessWeight
from profile_scraper.processTweets import addTweets
from profile_scraper.twitterQueries import buildProfile
from top_tweets import get_top_business_terms, get_top_personal_terms
from .models import Profile


"""
Index displays form to enter a twitter handle
"""
def index(request):
    if (Profile.objects.all().count() == 0):
        addUsers('Corporate-Account-Mapping-GoldSet.csv')
    users = Profile.objects.all()
    return render(request, 'profile_scraper/index.html', {'users' : users})

"""
Lookup takes a post request from index.html and parses the twitter handle from the form
Uses getProfile() to return a twitter profile object
"""
def lookup(request):
    twitterUserName = request.POST['twitterUserName']

    #Strip @ symbol from twitter username if it was sent through form
    if(twitterUserName[0] == '@'):
        twitterUserName = twitterUserName[1:]

    profile = Profile.objects.get(twitterUserName=twitterUserName)

    # If tweets have already been loaded for this user, skip
    if (profile.statuses_count == 0):
        tweets = determineTweetBusinessWeight(twitterUserName)
        top_business = get_top_business_terms(tweets)
        top_personal = get_top_personal_terms(tweets)
        profile.topBusinessTerms = top_business
        profile.topPersonalTerms = top_personal
        profile.save()
        addTweets(twitterUserName, tweets)
        buildProfile(twitterUserName)
        profile = Profile.objects.get(twitterUserName=twitterUserName)

    return render(request, 'profile_scraper/lookup.html', {'profile': profile})


def homepage(request):
    return render(request, 'profile_scraper/homepage.html')


