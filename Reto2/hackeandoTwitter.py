#Nuestros primeros pasos
import tweepy
import json

consumer_key = "7KTARRbzbbEM3vAS9biGHHwuI"
consumer_secret = "b2jIWHnSX85kGFmJcdaSwDyymOJIxJRFQ6aiswCD7lK0o68uRR"
access_token = "1276159765287141384-XYoJnxWCd8zD5ARDYbDjWx98cX0e0T"
access_toke_secret = "YKqSAJ2azFbcGR9Z8ZZtrjvBtx5vjcdS51c5oAnLW149t"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_toke_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#data = api.me()
user = api.get_user("Dani_artt")
#print (json.dumps(data._json, indsent=2))
i = 0
print(user.followers_count)
'''
for person in user.followers():
    print(i,person.screen_name)
    i += 1
'''