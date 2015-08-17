# W205-assignments
Turn stuff in to W205 (Arash)

# Assignment 2 Bucket
Please see the uploaded twitter files here:
s3://w205_hw2bucket

# Assignment 3
*files are in HW3 folder!*

-1.1 Creating db_restT
Key files: TweetToMongo.py, MongoGetSet.py
https://s3.amazonaws.com/w205_hw3bucket/tweets-q1.json

TweetToMongo.py is an adaptation of the TweetSerializer class from lecture. It's used in MongoGetSet.py to extract tweets and push them to the MongoDB collection.

-1.2 Creating db_tweets
Key files: S3toMongo.py, FollowersToMongo.py
https://s3.amazonaws.com/w205_hw3bucket/tweets-q2.json
FollowersToMongo.py is an adaptation of the TweetSerializer class from lecture. It was intended to be written with more functionality, but ended up being extremely similar to TweetToMongo.py. It's used in S3toMongo.py to extract tweets from AWS and store them in db_tweets.

-2.1 Top 30 Retweets

Key files: getTop30.py, FollowersToMongo.py
sorted entries in db_tweets by retweet_count.
The first half of getTop30.py finds the top 30 users and their locations after extracting a sorted list from db_tweets.


-2.2 Lexical Diversity

Key files: LexicalDiversity.py, LDplot.py, dbrestT_LDplot2.png
Grab list of all users from db_restT using simple find() method from pymongo. To expedite the process, I only downloaded 500 tweets for each user before calculating the lexical diversity. All the text was preprocessed to remove stopwords and symbols. LexicalDiversity.py was used to extract and store the data. LDplot.py was used to load the stored lexical diversities and output them as a .png barplot (using matplotlib). The output figure is dbrestT_LDplot2.png

-2.3 List of Followers of top 30 retweeted users stored in db_followers
Key files: getTop30.py, unfollowed.py

Collected followers ids over 12 hour difference. Only grabbed the list of followers ids for the top 30 (as opposed to all the users) in db_restT. Also limited number of followers_ids to 40000. Tried to have larger time gap between data collections, but initially used api.followers which took much longer (300 followers' pages every 15 minutes)and was prone to crashing due to lag in stream processing.  Later on, used api.followers_ids, which was much faster and reliable. Unfollowed.py extracted the top 10 users from db_restT and matched the list of followers from each of the two collections of followers_ids data (db_followers and db_followers2). The output is simply a printed statement of results.

-2.4 Sentiment Analysis
Key files: SentimentAnalysis.py, sentiment_train_dat.py

Training data was taken from the University of Michigan sentiment analysis Kaggle competition page :https://inclass.kaggle.com/c/si650winter11/data.
Applied logistic regression from scikit-learn with L2 regularization and C parameter of 1000 as derived from GridSearchCV. The model trained with 99% accuracy. However, after reviewing the predictions with actual twitter data, it is apparent the model is not able to match as accurately sports related tweets. This is likely due to the training data which consisted of tweets about books (e.g. Da Vinci Code). Accuracy could probably improve after preprocessing the text to remove stopwords and non-english characters or symbols. The naive bayes model tends to also be a more apt classifer for text than logistic regression.

-3
Key files: backups.py
https://s3.amazonaws.com/w205_hw3bucket/db_restT_backup_2015-07-20.json
https://s3.amazonaws.com/w205_hw3bucket/db_tweets_backup_2015-07-20.json

The backups.py file contains two functions, one that creates backups in S3 and another that loads from S3 back into mongodb. The reloading function has the backup files hardwired into a list and would be implemented within a for loop similar to the one used for the backup-to-s3 function.


# Assignment 4
- Part 1
To extract tweets, I wrote a scrapy program based off of the scrapy spider tutorial. The tweets were saved in a 'preprocessed' .csv file using the built-in writing function from scrapy (terminal command: scrapy crawl [spidername] -o output.csv).  Then I used a script called csv_clean_and_upload.py which reformatted the csv file to clean text and separate hashtags and urls for the MapReduce part. Then that output (WC2015.csv) was uploaded to S3 here: https://s3-us-west-2.amazonaws.com/w205hw4safyre/input/WC2015.csv

Note, no words were found to have occured more than 10000 times so I included words with over 1000 counts after the MR job.

1 Average length of tweets : 56 characters (in cleaning script)
2 top 20 urls: 
http://2.sas.com/6010BB7KI
http://2.sas.com/6014BB73y
http://2via.me/NPPIQkML11
http://2via.me/Nuhlu-XT11
http://2via.me/NztHzVbL11
http://2via.me/n0yHcaZ111
http://2via.me/n13e-AcT11
http://2via.me/n6F6OSML11
http://2via.me/n7s6OxyT11
http://2via.me/n8wf--R111
http://2via.me/nALjwcQT11
http://2via.me/nD9eD9wD11
http://2via.me/nGw2L7b111
http://2via.me/nNW89d8T11
http://2via.me/nSoR2aHT11
http://2via.me/ngNRP8S111
http://2via.me/nnvMLhwT11
http://365v.nl/1HeamDf
http://53eig.ht/1BU7NjE
http://53eig.ht/1GXaAwQ

3 Table of support tweets per team (assuming all tweets are supportive). USA is by far the most supported team
  - NOR 2118
  - CRC 661
  - ECU 784
  - NZL 1117
  - FRA 4101
  - JPN 5890
  - MEX 972
  - CHN 2451
  - SWE 2400
  - KOR 1103
  - GER 8911
  - SUI 1630
  - CAN 8211
  - CMR 1253
  - AUS 4338
  - ESP 765
  - NGA 2364
  - COL 2288
  - ENG 12072
  - NED 1841
  - USA 25438
  - CIV 1300
  - THA 1076
  - BRA 1603

4 Number of times USA and JPN co-occur: Japan--USA = 10, USA--Japan = 0.  This does not include hashtags, which would probably greatly increase the count. Number of times USA and champions co-occur = None found. This probably would be greater than 0 if #USA hadn't been removed.

- Part 2
Each of the MapReduce parts were implemented using separate MapX.py and ReducerX.py where 'X' represents the part number of the assignment and X = 1-4. The MapReduce was implemented using an EC2 cluster on AWS (AMI 3.8.0).  For each job, multiple part files were produced and had to be downloaded and analyzed to answer the questions in Part 2.  To expedite the process, I also analyzed the outputs locally via the terminal like so : "./MapX.py <input.csv |sort| ./ReducerX.py >output.txt"

