#!/usr/bin/env python
__author__ = 'Safyre'

'''
Code for part 4 of the Analysis.
Count the frequency of pairs of tweets
'''

import sys, os, re


#fields =['tweet_blob']

for line in sys.stdin:
    split_line = line.split(',')
    tweet = sorted(split_line[4].split())
    #print tweet
    for first_word, second_word in zip(tweet[0:len(tweet)-1], tweet[1:]): # have
            if first_word != second_word and (len(first_word)>1 and len(second_word)>1):
                print first_word + '\t' + second_word + '\t' + str(1)

'''
for page in df.tweet_blob:
    tweets = page.split(';') # list of tweets
    for tweet in tweets:
        #print tweet
        tweet = sorted(tweet.split())
        for first_word, second_word in zip(tweet[0:len(tweet)-1], tweet[1:]): # have
            if first_word != second_word and (len(first_word)>1 and len(second_word)>1):
                print first_word + '\t' + second_word + '\t' + str(1)
'''
