#import key modules
import tweepy
import pandas as pd

#Bearer Token inserted from gcp functions environment variables for twitter api access
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAADpAcAEAAAAAN9RKdHzdbTki26SRndWSkFNtZY8%3Ddllih5AeitkWwr9NitUkJRdyurMgDcBQeTZpawFOcaQ6EdK7z4')

# Get tweets that contain the hashtag #ikea
# -is:retweet exclude retweets
# lang:en for the tweets in english
query = '#ikea -is:retweet lang:en'
tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'], max_results=100)


#define function to get tweets to be run in gcp cloud functions
def get_tweets_ikea(tweets):
    '''
    1.This function gets the tweets we want from '#ikea' and saves the 3 required attributes to a pandas dataframe.
    2.Input params: tweets variable that contains the tweet search results via twitter api.
    3.Output params: a dataframe called df.
    '''
    try:
        list = []
        for tweet in tweets.data:
            list.append(tweet)

        df = pd.DataFrame(list)
        #df = df.drop('context_annotations',1) 
        return df
    except:
        raise Exception('Error in function get_tweets_ikea.')

df = get_tweets_ikea(tweets)
print(df)

'''
def bq_load(key, value):
  
  project_name = 'YOUR PROJECT NAME'
  dataset_name = 'YOUR DATASET NAME'
  table_name = key
  
  value.to_gbq(destination_table='{}.{}'.format(dataset_name, table_name), project_id=project_name')'''