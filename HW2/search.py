__author__ = 'Safyre'

import sys
import tweepy
import datetime
import urllib
import signal
import json

## Tweet Serializer, Will output tweets into .json files
class TweetSerializer:
   out = None
   first = True
   count = 0
   def start(self):
      #fname = "tweets-"+str(self.count)+".json"
      fname = "tweets-"+str(self.count)+".txt"
      self.out = open(fname,"w")
      #self.out.write("\n")
      self.out.write("[\n") #add bracket to open list
      self.first = True

   def end(self):
      if self.out is not None:
         self.out.write("\n]\n")
         self.out.close()
      self.out = None

   def write(self,tweet):
      if not self.first:
         self.out.write(",\n")
      self.first = False
      #json uses dictionary, "text" is key for content in tweet
      self.out.write(json.dumps(tweet._json["text"]))
      #self.out.write(json.dumps(tweet._json).encode('utf8'))
      self.count += 1 # count to save a new file

# connect to AWS
from boto.s3.connection import S3Connection
from boto.s3.key import Key # access bucket
#from bs4 import BeautifulSoup

###  Access Keys to Twitter API
consumer_key = "yL0bhBFTjCIzqP65khAWv3BDD";
consumer_secret = "6cFBpXLtV0VBmdKQZP8mTnbeQx6aMgXZtqokEiFEUNpRZKrPNT";

access_token = "3197773549-kljDxhJN0FGWnsXYUmIroM0QG5OVzhEgu8LTLHh";
access_token_secret = "nlIZhMZqmpSQrAqdn2foxRojKuJ6LmO8wUkDLIltuMQbM";

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler=auth)

### AWS S3 Bucket
bucket_name = "w205_hw2bucket"

## 3 Queries, need either the two, then both
q1 = urllib.quote_plus("#Warriors -#NBAFinals2015")  # URL encoded query
q2 = urllib.quote_plus("#NBAFinals2015 -#Warriors")
q3 = urllib.quote_plus("#NBAFinals2015 + #Warriors") # i hope the + works...

#q = q + urllib.quote_plus(" since 2015-06-07 until 2015-06-07")
# Additional query parameters:
#   since: {date}
#   until: {date}
# Just add them to the 'q' variable: q+" since: 2014-01-01 until: 2014-01-02"

## Open boto connection and create bucket
#from boto.s3.connection import S3Connection
#conn = S3Connection('AKIAJGEMM7IGTP4NTZCQ', 'k/Gi2aBpO5l/7+Y27peHU1bB/oiWyFR9ZbgYdxQG')
#bucket = conn.create_bucket('w205_hw2bucket')  # sub-datasets bucket already exists
#myBucket = conn.get_bucket('W205_HW2bucket')
#for key in myBucket.list():
#    print key.name.encode('utf-8')

# reopen file for set_contents_from_file to upload into S3
#fp = open("10-40.csv","r")

#myKey = Key(bucket)
#myKey.key = '10-40.csv'
#myKey.set_contents_from_file(fp)

#fp.close()



tweetSer = TweetSerializer()
tweetSer.start()
for tweet in tweepy.Cursor(api.search,q=q1, since = "2015-06-16", until = "2015-06-23", wait_on_rate_limit = True).items():
    tweetSer.write(tweet)
   # FYI: JSON is in tweet._json
    #print tweet._json
    print tweet.text

tweetSer.end()

#Iterate every two lines
#i = 0
#with old as f:
#    for line1,line2 in itertools.izip_longest(*[f]*2):
#    #from stackoverflow
    # ## Temporary file
#    t = tempfile.NamedTemporaryFile(mode="r+")
#    i += 1        name = ">" + str(i)
#    print name, line1.rstrip(), line2.rstrip()
#    t.write(name + "\n" + line1.rstrip() + "\n"+line2.rstrip()+"\n")