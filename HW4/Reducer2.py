#!/usr/bin/env python
__author__ = 'Safyre'

'''
reducer for part 1.  Read in printed text from Mapper.
relies on sorted data
./Map.py |sort|./wReducer.py'
'''

import sys

def tcount(prev_time, day, hour, counts):
    if prev_time is not None:
        print day + " " + hour + " count is: "+ str(counts)

prev_hour = None
prev_day = None
prev_time = None
counts = 0

for line in sys.stdin:
    day, hour, value = line.split('\t',2)
    time = day+" "+hour

    if time != prev_time:
        tcount(prev_time, prev_day, prev_hour, counts)
        prev_time = time
        prev_day = day
        prev_hour = hour
        counts = 0
    counts += eval(value)

tcount(prev_time, day, hour, counts)
