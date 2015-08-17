#!/usr/bin/env python
__author__ = 'Safyre'

'''
Code for part 2 of the Analysis.
Count the number of tweets per hour
'''

import sys, os, re


for line in sys.stdin:
    date = line.split(',')[1]
    if date.split()[1] == 'PM':
        hour = str(int(date.split(':')[0]) +12)
    else:
        hour = date.split(':')[0]
    day = date.split('-')[1]
    print day + '\t' + hour + '\t' + str(1)

