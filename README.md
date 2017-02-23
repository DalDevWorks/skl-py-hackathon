# skl-py-hackathon
DevWorks participated in [LeadSift's hackathon hosted by Shiftkey Labs](http://shiftkeylabs.ca/calendar/shiftkey-py-hackathon/) on Feb 22nd - Feb 24th 2017. 

LeadSift presented the following hackathon problems:

1. Find out where someone works based on info posted to their Twitter Profile.
2. Given just a company name (or website), can you determine if they are B2B or B2C?
3. How would you classify business vs personal tweets for Twitter profiles?

The two main hackathon requirements were:

- Use Python Django for the WebApp.
- Use the Twitter API to legally query the information.
- Use LeadSift's database CSV dump if needed.

After a brainstorming session and discussion within the organization, DevWorks chose to pursue problem 3: `Building a twitter profile classifier`.

## Twitter Classifier
We classify tweets from a given Twitter user in two types: `business` and `non-business`. We take information available through a LeadSift database CSV dump to generate a list of user candidates. From this list of candidates we select a user to investigate and then query the Twitter API to get all tweets posted by that user. Further, we use text pre-processing (punctuation, digits and stop-words) and a weighting algorithm to decide whether it's a business tweet or not. Finally, we display these tweets in two different lists in a view on the webpage.

## Setup and Installation Guide
This project uses Python 2.7. Make sure you have this version of Python installed, or use a VM (we recommend virtualenv) with Python 2.7 installed.

Follow this step-by-step guide to setup the environment:

1. Setup your development directory, e.g. `/dev/hackathons/shiftkey-py`, and `cd` into this directory.
2. Clone this repository: `git clone https://github.com/DalDevWorks/skl-py-hackathon.git`
3. `cd skl-py-hackathon`
4. `pip install django`
5. `pip install tweepy`
6. `pip install stop_words`

## Run the Server

1. Enter the following command: `python manage.py runserver`
2. Go to your favourite browser and enter this link: `127.0.0.1:8000/`

## DevWorks Team Member Participation

- Kirthy
- Eric
- Duncan
- Connor
- Sam
- Orjan
- Chaoran
