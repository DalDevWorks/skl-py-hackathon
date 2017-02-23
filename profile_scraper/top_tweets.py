from compute_ngrams import main
from businessTweetAlgorithm import determineTweetBusinessWeight

def get_top_business_terms(user_tweets):

    tweetProfile = user_tweets
    businessTweets = []


    for tweet in tweetProfile:
        if tweet['isBusiness'] > 0:
            businessTweets.append(tweet['processed_tweet'])

    main(businessTweets, 1.0, True, "business_results.txt", 10, 10, 3)

    business_file = open('business_results.txt', 'r')
    business_term_list = business_file.readlines()
    for term in business_term_list:
        term = term.rstrip('\n').split('|')
        print term

    top_terms = []
    top_terms.append(business_term_list)

    return top_terms

def get_top_personal_terms(user_tweets):

    tweetProfile = user_tweets
    personalTweets = []

    for tweet in tweetProfile:
        if tweet['isBusiness'] == 0:
            personalTweets.append(tweet['processed_tweet'])

    main(personalTweets, 1.0, True, "personal_results.txt", 10, 10, 3)

    personal_file = open('personal_results.txt', 'r')
    personal_term_list = personal_file.readlines()
    for term in personal_term_list:
        term = term.rstrip('\n').split('|')
        print term

    top_terms = []
    top_terms.append(personal_term_list)

    return top_terms

terms_list = get_top_business_terms(determineTweetBusinessWeight())
