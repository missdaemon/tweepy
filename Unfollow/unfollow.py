#! usr/bin/python

import tweepy
#from keys import *

screen_name = ""
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

followers  = api.followers_ids(screen_name)
friends = api.friends_ids(screen_name)

for f in friends:
    if f not in followers:
        print "Unfollow {0}?".format(api.get_user(f).screen_name)
        if raw_input("Y/N?") == 'y' or 'Y':
            api.destroy_friendship(f)
