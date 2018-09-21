# !/usr/bin/env python3
# (c) 2017 Landon A Marchant
"""
Use to discover the relationships between Twitter users.

CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, and ACCESS_TOKEN_SECRET are unique.
These keys belong to the dev account attached to @landonamarchant. Twitter enforces a rate limit.
If rate limit is reached, a "waiting" notification will be printed.

All input is case sensitive, do not include the @ symbol in front of usernames.

Args:
    User Input 1: First Twitter account to search. Must be a username.
    User Input 2: Second Twitter account to search for, within 1's followers.
    User Input 3: Third Twitter account to search for, within 2's followers.

Returns:
    A list of users following 1.
    A printed statement saying whether or not 2 is following 1.
    A printed statement saying the relationship between 3, 2, and 1.

Raises:
    Rate limit notification:
        Raised when too many requests have been made.
        Sometimes it's best to end the program, wait 15+ minutes, then run again.

    User Input:
        Program will not work if User Input is not a username. API returns an error.
To Do:
    Create loop that prevents API error (tweepy.error.TweepError) and asks for proper input.
    Build when statement to prevent timeout errors through increasing wait times.
        "Waiting longer" may or may not succeed, mixed results have been reported online.
"""

import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(AUTH, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

print("Twitter usernames are case sensitive. Input must be a username. Do not include the '@'.")
# todo: create loop that prevents tweepy.error.TweepError.
# loop will eventually print "Input is not a valid screen name.
# prompt for user input will be "Please enter a valid screen name: "
searched_account = input("First Twitter screen name to search: ")

  # Cursor travels through pages of followers.
users = tweepy.Cursor(api.followers, screen_name=searched_account, include_entities=True).items()

followers = [profile.screen_name for profile in users]
users = [api.get_user(name) for name in followers]
fuids = [user.id for user in users]

print("Followers are: {}".format(sorted(followers, key=str.lower)))

looking_for = input("Which of {}'s followers would you like to look for: ".format(searched_account))

if looking_for in followers:
    print("{} is in {}'s list of followers".format(looking_for, searched_account))
if looking_for not in followers:
    print("{} is not in {}'s list of followers".format(looking_for, searched_account))

user_two = tweepy.Cursor(api.followers, screen_name=looking_for, include_entities=True).items()
second_follower = [profile.screen_name for profile in user_two]
users_REPAIR = [api.get_user(name) for name in second_follower]
fuids2 = [follow_two.id for follow_two in users_REPAIR]

second_user = input("Which account would you like to find in {}'s followers? ".format(looking_for))

for second_user in user_two:

    print("{} follows {}, who follows {}. ".format(second_user, looking_for, searched_account))
if second_user not in user_two:
    print("{} does not follow {}. {} does follow {}. ".format(second_user, looking_for, looking_for, searched_account))
