![DevWorks](https://github.com/DalDevWorks/skl-py-hackathon/blob/master/devworklogo.png)
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

1. Install Virtualenv: `sudo pip install virtualenv`
2. Create a directory for the virtual environment: `cd ~/` and `mkdir envs`
3. Create the hackathon virtual environment: `virtualenv —-system-site-packages ~/envs/skl-py-hackathon` (sometimes there is an issue when copying and pasting this command. It works when typing it manually. Remember the double dashes.)
4. Before doing any development, enter the virtual environment: `source ~/envs/reviewboard-3.0/bin/activate`. Optional: Create an alias for activating the VM: `vim .bash_profile` and add this `alias hack-skl-py='source ~/envs/skl-py-hackathon/bin/activate'`. You can now access the virtual environment from any directory by typing the command `hack-skl-py`.
5. Setup your development directory, e.g. `/dev/hackathons/shiftkey-py`, and `cd` into this directory.
6. Clone this repository: `git clone https://github.com/DalDevWorks/skl-py-hackathon.git`
7. `cd skl-py-hackathon`
8. `pip install django`
9. `pip install tweepy`
10. `pip install stop_words`

## Run the Server

1. Make sure you are in the app directory, e.g: `cd dev/hackathons/skl-py-hackathon`
2. Run the DB migrations if you haven't already done so: `python manage.py migrate`
3. Start the server: `python manage.py runserver`
4. Click on this link: [Localhost](http://127.0.0.1:8000/)

## DevWorks Team Member Participation

- Kirthy Kumar
- Eric Desjardins
- Duncan Pulsifer
- Connor Walsh
- Samyse Jawich
- Orjan Monsen
- Chaoran Zhou

## Guest Member Participation
- Dylan Seitz
