__author__ = 'Safyre'


import os, pymongo, json
from boto.s3.key import Key
from boto.s3.connection import S3Connection
from amazonkeys import *

print "connecting to S3 via boto \n"
conn = S3Connection(awsPublicKey, awsSecretKey)
print "Connected!"

firstBucket = conn.get_bucket('w205hw4safyre')

local_path = os.getcwd()
filelist = []


# used this to analyze word counts

print "Part 1 download"
for key in firstBucket.list():

    endswith = ["0", "1", "2", "3", "4", "5", "6"]
    for i in endswith:
        if str(key.name).endswith("part-0000"+i):
            filepath = local_path + '/job1/' + str(key.name.encode('utf-8').split('/')[-1] +'.txt')
            print filepath
            try:
                key.get_contents_to_filename(filepath)
                filelist.extend(str(key.name))
            except OSError:
                print "error downloading file to", filepath



print "Part 1 Analysis: number of words with over 10000 occurrences \n"


count = 0

with open("output1.txt", 'r') as f:
    for line in f.readlines():
        if line.split()[-1]>10000:
            count +=1
print "Number of words with over 1000 occurrences:", count



print "Part 3 Analysis: top 20 urls \n"

urls = []
counts = []
with open("output3.txt", 'r') as f:
    for line in f.readlines():
        urls.append(line.split()[0])
        counts.append(line.split()[-1])

sortedurls = [list(x) for x in zip(*sorted(zip(urls, counts), key=lambda pair: pair[1]))]
#print sortedurls
print "Top 20 urls: \n"
for url in sortedurls[0][0:20]:
    print url


