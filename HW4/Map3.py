#!/usr/bin/env python
__author__ = 'Safyre'

'''
Code for part 3 of the Analysis.
Count the top 20 urls
'''

import sys

for line in sys.stdin:
    split_line = line.split(',')
    if split_line[2] != '':
        print split_line[2] + '\t' + str(1)

