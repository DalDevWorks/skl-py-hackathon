#!/usr/bin/python

import tweepy
from .models import Profile

# Twitter API credentials
consumer_key = "voX3ehOFjwgAVmFSa1s8xSwif"
consumer_secret = "1UiPMzPjNqSXGH3UVhoOnS7FOnunO2LeNRAg5Koih2YLQJercb"
access_key = "135690860-gbiRRkjxvci1lyOjww2ROZeWtCk0dfeOzUMiVtB9"
access_secret = "zWkXZxYkxfYWspubIVj5PeT8r53di1bBf75M6pjT74BUt"


def getProfile(handle):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        # https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(handle)
    except:
        user_profile = "User Profile Not Found"

    return user_profile


def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        # print "...%s tweets downloaded so far" % (len(alltweets))
    outtweets = [[tweet.id_str, tweet.text.encode("utf-8")] for tweet in alltweets]

    tweetData = []

    for tweet in outtweets:
        data = {}
        data['id'] = tweet[0]
        data['tweet'] = tweet[1]
        tweetData.append(data)

    # You can access tweetData with tweetData[1]['tweet']

    return tweetData

def buildProfile(screen_name):
    user = Profile.objects.get(twitterUserName=screen_name)
    twitter_profile = getProfile(screen_name)

    user.description = twitter_profile.description
    user.followers_count = twitter_profile.followers_count
    user.following_count = twitter_profile.following
    user.friends_count = twitter_profile.friends_count
    user.profile_image_url = twitter_profile.profile_image_url
    user.save()







