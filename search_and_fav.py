# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 14:39:54 2014

@author: jmcontreras
"""

# Import modules
import sys
import twitter

def main(query, count):
    
    # Provide authorization credentials
    token_key = 'YOUR_TOKEN_KEY'
    token_secret = 'YOUR_TOKEN_SECRET'
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    
    # Connect to Twitter API
    auth = twitter.OAuth(token_key, token_secret, consumer_key, consumer_secret)
    t = twitter.Twitter(auth=auth)
    
    # Search tweets
    def search(query, count, max_id=None):
        return t.search.tweets(q=query, result_type='recent', count=count, max_id=max_id)
    
    # Favorite tweet
    def fav(tweet):
        try:
            result = t.favorites.create(_id=tweet['id'])
            print "Favorited: %s" % (result['text'])
            return result
        except twitter.TwitterHTTPError as e:
            print "Error: ", e
            return None
    
    # Search and favorite tweets
    def search_and_fav(query, count, max_id=None):
        result = search(query, count, max_id)
        success = 0
        for t in result['statuses']:
            if fav(t) is not None:
                success += 1
        print "Favorited: %i of %i" % (success, len(result['statuses']))
    
    # Run the program
    search_and_fav(query, count)
        
if __name__ == '__main__':
    
    count = int(sys.argv.pop(-1))
    query = sys.argv[1:]
    main(query, count)
