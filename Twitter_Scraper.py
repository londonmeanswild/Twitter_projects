#  !/ur/bin/env python3
#  Landon A Marchant

""" Uses BeautifulSoup to scrape for tweets.

    Args:

    Returns:

    Raises:

    Important Authorization Information:
    Tweets saved in: 
"""
#  create CSV database
#import csv
#import sys

from pylint import epylint as lint
import time
from urllib2 import urlopen
import requests
from bs4 import BeautifulSoup, NavigatableString #unable to import bs4

"""pylint says invalid module name, and missing docstring. 
I need to write some kind of class or function,
but I am not sure what to call it or how to do this.
It feels like I have a lot of different steps,
and they're not really connected."""

RESULTS_PER_PAGE = 15

print "Twitter Username:"
user = raw_input() #invalid constant name "user"
endpoint = "https://twitter.com/%s" 

f = urlopen(endpoint % user)
html = f.read() #  invalid constant name "f". "html"
f.close()

soup = BeautifulSoup(html, 'html.parser') #  invalid constant name "soup"

tweets = soup.findAll('strong', {'class': 'fullname js-action-profile-name-show-popup-with-id'})
#  "invalid constant name "tweets"
#  line 43 missing function docstring, unused argument "number of tweets"


SEARCH_URL = u'https://twitter.com/realDonaldTrump?page=%s'

def get_tweets(search_query, number_of_tweets):
    search_query = search_query.replace(' ', '+')
    results_list = [0]

for i in range(0, number_of_tweets, -1, RESULTS_PER_PAGE):
    results = RESULTS_PER_PAGE
    remaining_tweets = number_of_tweets - start_tweet
    
    if remaining_tweets < RESULTS_PER_PAGE:
        results = remaining_tweets

    page = requests.get(SEARCH_URL % (start_tweet, search_query, results))
    success = False

r = requests.get(url + query)
soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]
action_tag = soup('span', {'class': 'username js-action-profile-name'})
show_name = action_tag[i].content[1].contents[0]

 #  results_list = tweets[i].contents[0]
    #  twitter_text = soup('p'. {'class': 'js-tweet-text'}) do not need this for current project







# first create CSV

"""file = open(sys.argv[1]. 'wt')
try: 
    writer = csv.writer(f)
    writer.writerow( ('@username', 'date', 'hashtag'))
    for i in range():
        writer.writerow ()

"""

