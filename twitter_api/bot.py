import sys
import time
import tweepy
import json

fin = open("file.txt", "r") # Opening the source text.
with open('config.json') as data_file:  # Opening the secret file (contains tokens)
    secret = json.load(data_file)

# Twitter keys for autentication
apiKey = secret["Twitter"]["apiKey"]
apiSecret = secret["Twitter"]["apiSecret"]
accessToken = secret["Twitter"]["accesToken"]
accessTokenSecret = secret["Twitter"]["accesTokenSecret"]

auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)
api.update_status('Twitter bot reporting in live');

tweets = api.mentions_timeline()
print(tweets)

for tweet in tweets:
    if '#URGENT' in tweet.text.lower():
        print(str(tweet.id)+ ' - '+ tweet.text)