import json
import pandas as pd
import matplotlib.pyplot as plt


tweets_data_path = 'cola_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print(len(tweets_data))
for i in range(len(tweets_data)):

    if(tweets_data[i]['lang'] == 'en'):
        print(tweets_data[i]['text'])
        print('--------------\n')
