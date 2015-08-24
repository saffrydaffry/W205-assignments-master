__author__ = 'Safyre'

'''
Clean up csv file then upload to S3 as WWCFIFA.csv
Output of scrapy spider is a table with each row representing a page of 20 tweets.

-page_dates, 20 or so dates for each tweet in H:MM PM - D Mon YYYY format separated by ','
-min_id, the bottom-most tweet id of the page
-tweet_texts, all tweets delimited by ';' within a page
-page_texts, tweet text without a delimiter or linked text
-page_links, links (href) only for the whole page (including hashtags)
-page_linktxts, texts for each link for each page

'''
import os, math, json, csv, string, re
from filechunkio import FileChunkIO
from amazonkeys import *
from boto.s3.key import Key
from boto.s3.connection import S3Connection

import csv
print "Restructuring dates for Part 2:\n"

with open('twitterFIFA/preWC2015.csv', 'rb') as csvfile:
    twitter_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    twitter_reader.next() #skip header
    output = open('WC2015.csv', 'wb')
    tweet_writer = csv.writer(output)
    tweet_len = []
    hashtag_dic = {}
    for row in twitter_reader:
        new_row = []
        user_id = row[0]
        new_row.append(user_id)

        date    = row[1]
        new_row.append(date)

        tweet   = row[2]
        #new_row.append(tweet) #confuses map reduce which splits on commas

        urls    = ' '.join(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet))
        new_row.append(urls)

        hashtag = ' '.join(re.findall('\S*#(?:\[[^\]]+\]|\S+)', tweet))
        hashtag = re.sub('\,','', hashtag)

        for hash in hashtag.split():
            teams = ['#CAN', '#FRA', '#USA', '#KOR', '#GER', '#AUS', '#ENG', '#JPN', '#CHN', '#SUI', '#NOR', '#SWE', '#NED', '#ESP', '#NGA', '#CMR', '#CIV', '#THA', '#NZL', '#BRA', '#COL', '#ECU', '#COL', '#CRC', '#MEX']
            if hash in teams:
                hashtag_dic[hash] = hashtag_dic.get(hash,0)+1

        new_row.append(hashtag)

        ## create a cleaned up tweet
        tweet_blob = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet)
        #print tweet_blob
        tweet_blob = re.sub('\S*#(?:\[[^\]]+\]|\S+)', '', tweet_blob)
        tweet_blob = re.sub('pic.twitter.com/\w+', '', tweet_blob)
        tweet_blob = re.sub('(\@)\w+', '', tweet_blob)
        tweet_blob = re.sub('[\.\,\n\!\?\r\t]', '', tweet_blob)
        #print tweet_blob
        tweet_sep = tweet_blob.split()
        tweet_blob = ' '.join([n for n in tweet_sep if n.isalpha()]).lower()
        new_row.append(tweet_blob)

        tweet_writer.writerow(new_row)
        tweet_len.append(len(tweet_blob))
        #print new_row
        #print tweet_blob + '\n'
        #print  row #', '.join(row)

print "Average length of tweets: ", float(sum(tweet_len))/len(tweet_len)

print "Table of hashtag messages counts:"
for key, value in hashtag_dic.iteritems():
    print key, value

'''
## UPlOAD
print "connecting to S3 via boto \n"
conn = S3Connection(awsPublicKey, awsSecretKey)
bucket = conn.create_bucket('w205_hw4bucket_input')
myBucket = conn.get_bucket('w205_hw4bucket_input')

# Get file info
source_path = '/Users/Safyre/Documents/W205-assignments-master/HW4/WC2015.csv'

fp = open(source_path, "r")
myKey = Key(bucket)
myKey.key = "WC2015.csv"
myKey.set_contents_from_file(fp)
fp.close()
print "done with upload!"
'''
