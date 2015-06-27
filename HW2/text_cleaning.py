__author__ = 'Safyre'
import nltk
from nltk.corpus import stopwords
import matplotlib as plt
from matplotlib.pyplot import savefig
import os

import math, os
from boto.s3.key import Key
from filechunkio import FileChunkIO
from boto.s3.connection import S3Connection

print "connecting to S3 via boto \n"
conn = S3Connection('AKIAJGEMM7IGTP4NTZCQ', 'k/Gi2aBpO5l/7+Y27peHU1bB/oiWyFR9ZbgYdxQG')
wkdir = '/Users/Safyre/Documents/W205-assignments-master/HW2/'
#bucket = conn.create_bucket('w205_hw2bucket')  # sub-datasets bucket already exists
myBucket = conn.get_bucket('w205_hw2bucket')
myKey = Key(myBucket)
bucket_list = myBucket.list()
# awesomeness http://www.laurentluce.com/posts/upload-and-download-files-tofrom-amazon-s3-using-pythondjango/
print "downloading new files locally\n"
print "like this: s3_oldfilename.txt"

for l in bucket_list:
  keyString = str(l.key)
  # check if file exists locally, if not: download it
  if not os.path.exists(wkdir+"s3_"+keyString):
    l.get_contents_to_filename(wkdir+"s3_"+keyString)


#outputs from search.py have the following issues that need to be resolved
# - Open and closing brackets around text blob
# - unicode characters "\" "\n" "\u..."
# - stopwords
os.getcwd()
## For Q1

print("Getting file for #Warriors only\n")
tweet_file = open("s3_tweets-q1.txt", "r")
# List words from  the file contents
tweet_blob = tweet_file.read().split()

print ("Here's a piece of it before we process... \n")
print tweet_blob[:100]
# make all words lowercase, non-funky numbers/symbols, and not a stop word
print("Calculating frequency distribution using nltk...\n")
print("Here we remove English stopwords and all non-alphanumeric characters\n")
print("This takes awhile, please feel free to grab lunch")
#fd = nltk.FreqDist([word.lower() for word in tweet_blob if word.isalpha() & (word.lower() not in stopwords.words('english'))]) #count

print("Plotting the top 25 words")
print("Please save and close this beautiful masterpiece!")
#fd.plot(25) #plot counts


## For Q2
print("Getting file for #NBAFinals2015 only\n")
tweet_file = open("s3_tweets-q2.txt", "r")

# List words from  the file contents
tweet_blob = tweet_file.read().split()

print("Calculating frequency distribution using nltk...\n")
print("Here we remove English stopwords and all non-alphanumeric characters\n")
# make all words lowercase, non-funky numbers/symbols, and not a stop word
fd = nltk.FreqDist([word.lower() for word in tweet_blob if word.isalpha() & (word.lower() not in stopwords.words('english'))]) #count
print("Plotting the top 25 words")
print("Please save and close this beautiful masterpiece!")
fd.plot(25) #plot counts


## For Q3
print("Getting file for Both #Warriors and #NBAFinals2015 \n")
tweet_file = open("s3_tweets-q3.txt", "r")

# List words from  the file contents
tweet_blob = tweet_file.read().split()

print("Calculating frequency distribution using nltk...\n")
print("Here we remove English stopwords and all non-alphanumeric characters\n")
# make all words lowercase, non-funky numbers/symbols, and not a stop word
fd = nltk.FreqDist([word.lower() for word in tweet_blob if word.isalpha() & (word.lower() not in stopwords.words('english'))]) #count
print("Plotting the top 25 words")
print("Please save and close this beautiful masterpiece!")
fd.plot(25) #plot counts



