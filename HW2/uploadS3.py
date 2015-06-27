__author__ = 'Safyre'

import math, os
from boto.s3.key import Key
from filechunkio import FileChunkIO
from boto.s3.connection import S3Connection

print "connecting to S3 via boto \n"
conn = S3Connection('AKIAJGEMM7IGTP4NTZCQ', 'k/Gi2aBpO5l/7+Y27peHU1bB/oiWyFR9ZbgYdxQG')
bucket = conn.create_bucket('w205_hw2bucket')  # sub-datasets bucket already exists
myBucket = conn.get_bucket('w205_hw2bucket')

#for key in myBucket.list():
#    print key.name.encode('utf-8')


#print "uploading #Warriors only.  This is a big file, so we'll upload it in two parts"

# Get file info
source_path = '/Users/Safyre/Documents/W205-assignments-master/HW2/tweets-q1.txt'
source_size = os.stat(source_path).st_size

# Create a multipart upload request from boto tutorial
mp = myBucket.initiate_multipart_upload(os.path.basename(source_path))

# Use a chunk size of 50 MiB (feel free to change this)
chunk_size = source_size / 2
chunk_count = int(math.ceil(source_size / float(chunk_size))) ## is 2

# Send the file parts, using FileChunkIO to create a file-like object
# that points to a certain byte range within the original file. We
# set bytes to never exceed the original file size.
# source here http://boto.readthedocs.org/en/latest/s3_tut.html
print "Loading each chunk...\n"
for i in range(chunk_count):
    offset = chunk_size * i
    bytes = min(chunk_size, source_size - offset)
    with FileChunkIO(source_path, 'r', offset=offset,
                     bytes=bytes) as fp:
        mp.upload_part_from_file(fp, part_num=i + 1)

#Finish the upload
mp.complete_upload()
print "done with part 1!"

print "the other parts are much smaller, so no chunking needed \n"
print "Unlike with the previous method using FileChunkIO to upload the file by parts, \n here I needed to explicitly name the file in S3"
print "Begin uploading #NBAFinals2015 only\n"
# reopen file for set_contents_from_file to upload into S3
source_path = '/Users/Safyre/Documents/W205-assignments-master/HW2/tweets-q2.txt'
fp = open(source_path, "r")
myKey = Key(bucket)
myKey.key = "tweets-q2.txt"
myKey.set_contents_from_file(fp)
fp.close()
print "done with part 2!"

print "Begin uploading #NBAFinals2015 only\n"
# reopen file for set_contents_from_file to upload into S3
source_path = '/Users/Safyre/Documents/W205-assignments-master/HW2/tweets-q3.txt'
fp = open(source_path, "r")
myKey.key = "tweets-q3.txt"
myKey.set_contents_from_file(fp)
fp.close()
print "done with part 3!"



