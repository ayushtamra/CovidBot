import tweepy
from auth import authenticate, authenticate_search
import json
from add_to_db import upload_data, is_exists_in_database
from tweet_entity import TweetEntity
import requests
from config import FIREBASE_URL, FIREBASE_NEW_URL
import json
from time import sleep
import random
from dateutil.parser import parse

with open("cities", "r") as f:
    cities = f.read().split("\n")
    cities = cities[:30]

keywords = ['oxygen', 'remdesivir', 'icu', 'hospital beds', 'plasma']
search_keyword = "verified"
ignore_keywords = "-needed -required -leads -requirement -need -please"
ignore_bots = "-ShariqueAly -findthecolors"
filter_out = "-filter:retweets"

auth = authenticate_search()
api = tweepy.API(auth, wait_on_rate_limit=True)