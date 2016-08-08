import tweepy

consumer_key = "here goes the consumer key"
consumer_secret = "here goes the consumer secret key"
access_token = "here goes a token"
access_token_secret = "here goes the secret token"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

x = tweepy.API(auth)
for tweets in x.home_timeline(count=10):
 print(tweets.created_at)
 print(tweets.user.screen_name)
 print(tweets.text)
 print('*'*40)
