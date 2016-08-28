#testing 02 trying printing the timeline and acount info :)
import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print("MY TWITTER TIMELINE")

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print("[+] %s" % tweet.text)
    
print("Información de Cuenta de Twitter")

# Get the User object for twitter...
user = api.get_user('misconception')
print("Nombre de Perfil: ", user.screen_name)
print("Cantidad de Followers:", user.followers_count)
for friend in user.friends():
    print("Lista de Amigos de ",user.screen_name,": ", friend.screen_name)
