import tweepy
import re
from textblob import TextBlob
import csv

consumer_key ='####'
consumer_secret ='####'

access_token = '####'
access_token_secret = '####'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
public_tweets =  api.search('Corona', tweet_mode='extended', lang='en')

def clean_tweet(tweet): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) (\w+:\/\/\S+)", " ", tweet).split()) 

 
with open("sentimentvalues.csv", "wb") as sentimentFile:
	sentimentFileWriter = csv.DictWriter(sentimentFile,delimiter=',', fieldnames = ["Tweets", "Sentiment"]);
	sentimentFileWriter.writeheader()
sentimentFile.close();
        
with open("sentimentvalues.csv", "ab") as sentimentFile:
	sentimentFileWriter = csv.writer(sentimentFile,delimiter=',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
	
	for tweet in public_tweets:
		analysis= TextBlob(clean_tweet(tweet.full_text))

		if analysis.sentiment.polarity > 0:
		    sentimentFileWriter.writerow([tweet.full_text.encode('utf8'), "Positive"])
	 	elif analysis.sentiment.polarity < 0:
	 	    sentimentFileWriter.writerow([tweet.full_text.encode('utf8'), "Negative"])
	 	else: 
	 		sentimentFileWriter.writerow([tweet.full_text.encode('utf8'), "Neutral"])

sentimentFile.close();

    

