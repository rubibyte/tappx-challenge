import pandas as pd
import time


df = pd.read_csv('tweets.csv', encoding='cp1252').text

def tweets(tweets):
    for tweet in tweets:
        yield tweet

for tweet in tweets(df):
    print(tweet)
    time.sleep(2)








