#!/usr/bin/env python
__author__ = 'Safyre'

'''
Code for part 1 of the Analysis.
Count the number of words with over 10000 occurrances
'''

import sys, os, re

for line in sys.stdin:
    split_line = line.split(',')
    #split_line = re.split(r', (?=(?:"[^"]*?(?: [^"]*)*))|, (?=[^",]+(?:,|$))', line)
    #print split_line[4]
    for word in split_line[4].split():
        print word.strip() + '\t' +str(1)
