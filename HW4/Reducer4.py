#!/usr/bin/env python
__author__ = 'Safyre'

import sys, os, re, math
import pandas as pd

import sys

#def PMI(first_count, second_count, paired_count):
#    return math.log10(paired_count/(first_count*second_count))

#def wcount(prev_1, prev_2, first_count, second_count, paired_count):
#    if prev_1 is not None:
#        print prev_1 + " count is "+ str(counts)

def wcount(prev_pair, first_word, second_word, paired_count):
    if prev_pair is not None:
        print first_word + "--" + second_word + '\t'+ str(paired_count)

pair = None
prev_pair = None

prev_1 = None
prev_2 = None

#first_count = 0
#second_count = 0
paired_count = 0

for line in sys.stdin:
    first_word, second_word, value = line.split('\t')
    pair = first_word +second_word
    if pair != prev_pair:
        wcount(prev_pair, prev_1, prev_2, paired_count)
        prev_pair = pair
        prev_1 = first_word
        prev_2 = second_word
        paired_count = 0

    paired_count += eval(value)

wcount(prev_pair, first_word, second_word, paired_count)
