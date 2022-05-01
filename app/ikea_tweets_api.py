#import key modules
import tweepy
import pandas as pd
from pandas.io import gbq
import pandas_gbq

#load data into bigQuery db from df
def bq_load(key, value):
  """
  Function loads data into bq from pandas df.
  """
  project_name = 'sigma-scheduler-348710'
  dataset_name = 'ikea'
  table_name = key
  
  value.to_gbq(destination_table='{}.{}'.format(dataset_name, table_name), project_id=project_name, if_exists='append')

#define function to get tweets to be run in gcp cloud functions
def get_tweets_ikea(data, context):
    '''
    This function gets the tweets we want from '#ikea' and saves the 3 required attributes to a pandas dataframe.
    Input params: data and context - default for cloud functions triggered by gcs. param is request for http.
    '''
    #Bearer Token inserted from gcp functions environment variables for twitter api access
    client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAADpAcAEAAAAAN9RKdHzdbTki26SRndWSkFNtZY8%3Ddllih5AeitkWwr9NitUkJRdyurMgDcBQeTZpawFOcaQ6EdK7z4')
    data = data
    context = context
    # Get tweets that contain the hashtag #ikea
    # -is:retweet exclude retweets
    # lang:en for the tweets in english
    query = '#ikea -is:retweet lang:en'
    tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'], max_results=100)
    try:
        list = []
        for tweet in tweets.data:
            list.append(tweet)
        df = pd.DataFrame(list)
        bq_load('ikea_table_data', df)
    except:
        raise Exception('Error in function get_tweets_ikea.')