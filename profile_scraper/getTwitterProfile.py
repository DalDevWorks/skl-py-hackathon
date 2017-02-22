#!/usr/bin/python

import tweepy

def getProfile(handle):

    # Twitter API credentials
    consumer_key = "voX3ehOFjwgAVmFSa1s8xSwif"
    consumer_secret = "1UiPMzPjNqSXGH3UVhoOnS7FOnunO2LeNRAg5Koih2YLQJercb"
    access_key = "135690860-gbiRRkjxvci1lyOjww2ROZeWtCk0dfeOzUMiVtB9"
    access_secret = "zWkXZxYkxfYWspubIVj5PeT8r53di1bBf75M6pjT74BUt"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        # https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(handle)
    except:
        user_profile = "User Profile Not Found"

    return user_profile



