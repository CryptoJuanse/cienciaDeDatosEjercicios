#Nuestros primeros pasos
import tweepy
import json

#Datos para la autenticacion
consumer_key = "7KTARRbzbbEM3vAS9biGHHwuI"
consumer_secret = "b2jIWHnSX85kGFmJcdaSwDyymOJIxJRFQ6aiswCD7lK0o68uRR"
access_token = "1276159765287141384-XYoJnxWCd8zD5ARDYbDjWx98cX0e0T"
access_toke_secret = "YKqSAJ2azFbcGR9Z8ZZtrjvBtx5vjcdS51c5oAnLW149t"

#Conectando con la API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_toke_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

'''#Imprimir la linea de tiempo de mi usuario
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

#Informacion basica de un usuario
user = api.get_user('N_Navarro_M')
print(user.screen_name)
print(user.followers_count)

#Obteniendo informacion atraves del cursor (friends/followers)
for friend in tweepy.Cursor(api.followers, screen_name=user.screen_name).items(100):
    print(friend.screen_name)

#Obtener un timeline
for tweet in tweepy.Cursor(api.user_timeline, screen_name=user.screen_name,).items(10):
    print(tweet.text)

#Buscar Tweets
for tweet in tweepy.Cursor(api.search, q="covid", tweet_mode="extended").items(50):
    print(tweet._json['full_text'])'''

#Extrayendo 100 tweets de un usuario
publicaciones = api.user_timeline(screen_name="MLPiraquive", count=100, lang='es', tweet_mode='extended')

#Imprimir los ultimos 5 tweet de la cuenta
print('Ultimos tweets: \n')
for tweet in publicaciones[0:5]:
    print(tweet.full_text + '\n')