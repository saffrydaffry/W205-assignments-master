__author__ = 'Safyre'
## count the number of unique tags in each folder
# from stack overflow
import os  # imports terminal commands


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# local_results = open("out/part-00000", 'r')

print file_len("out/part-00000")

os.system("cd ~/cc-mrjob/out")
os.system("less *|grep 'address' ")

## use file compare module to see if the outputs are identical

import filecmp
# first need to append all the emr-out files to one
import glob

os.system("cd emr-out")
#read_files = glob.glob("*.txt")
read_files = ['emr-out/part-00000', 'emr-out/part-00001', 'emr-out/part-00002', 'emr-out/part-00003',
              'emr-out/part-00004', 'emr-out/part-00005', 'emr-out/part-00006', 'emr-out/part-00007',
              'emr-out/part-00008', 'emr-out/part-00009', 'emr-out/part-00010']

with open("result.txt", "r+") as outfile:
    for f in read_files:
        with open(f, "r") as infile:
            outfile.write(infile.read())

outfile.close()
infile.close()
# result.txt is not sorted, sort them the same way?
import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

#sorting result
result =  natural_sort(open("result.txt", "r"))
with open("result2.txt", "r+") as outfile:
    for item in result:
        outfile.write(item)
outfile.close()

#sorting part-00000
part0 =  natural_sort(open("out/part-00000", "r"))
with open("part_sort.txt", "r+") as outfile:
    for item in part0:
        outfile.write(item)
outfile.close()

filecmp.cmp('result2.txt', 'part_sort.txt') #returns TRUE

# Have same number of lines
file_len("part_sort.txt")
file_len("result2.txt")