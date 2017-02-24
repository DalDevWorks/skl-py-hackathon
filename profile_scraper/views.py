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
        get_top_business_terms(tweets)
        get_top_personal_terms(tweets)

        top_business = []
        with open('business_results.txt', 'r') as b_top:
            for i in range(3):
                line, freq = b_top.next().rsplit('|')
                top_business.append(line)
                top_business.append(freq)

        top_personal = []
        with open('personal_results.txt', 'r') as p_top:
            for i in range(3):
                line, freq = p_top.next().rsplit('|')
                top_personal.append(line)
                top_personal.append(freq)

        profile.topPersonalTerms = ','.join(top_personal)
        profile.topBusinessTerms = ','.join(top_business)
        profile.save()
        addTweets(twitterUserName, tweets)
        buildProfile(twitterUserName)
        profile = Profile.objects.get(twitterUserName=twitterUserName)

    b1,bf1,b2,bf2,b3,bf3 = profile.topBusinessTerms.rsplit(',')
    p1,pf1,p2,pf2,p3,pf3 = profile.topPersonalTerms.rsplit(',')

    return render(request, 'profile_scraper/lookup.html', {'profile': profile,
                                                           'b1': b1,
                                                           'bf1':bf1,
                                                           'b2': b2,
                                                           'bf2':bf2,
                                                           'b3':b3,
                                                           'bf3':bf3,
                                                           'p1':p1,
                                                           'pf1':pf1,
                                                           'p2':p2,
                                                           'pf2':pf2,
                                                           'p3':p3,
                                                           'pf3':pf3
                                                           })


def homepage(request):
    return render(request, 'profile_scraper/homepage.html')


