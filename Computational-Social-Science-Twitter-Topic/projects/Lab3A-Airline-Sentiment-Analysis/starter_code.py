# Import necessary modules
import os
import tweepy as tw
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from scipy import stats
from textblob import TextBlob
from tweepy import OAuthHandler
from IPython.display import display, HTML

# 1.md and 2.md
consumer_key = "Your key goes here!"
consumer_secret = "Your key goes here!"
access_token = "Your key goes here!"
access_token_secret = "Your key goes here!"

# Search dictionary to pass into produce_dataframe() as airlines to search for. DO NOT EDIT!
search_dict = {"Spirit Airlines": "#spiritairlines","JetBlue": "#jetblue", "Frontier Airlines": "frontier airlines", 
             "Delta": "delta airlines", "United": "united airlines", "Southwest": "southwest airlines", "American": 
             "american airlines"
            }

# The date to search from 
date_since = "This date should be five days from now!"
d = datetime.date.today()
print(d)
# Check that the tweepy object is working!
