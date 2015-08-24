#!/usr/bin/env python
__author__ = 'Safyre'

import sys, os, re
import pandas as pd

import sys

def wcount(prev_word, counts):
    if prev_word is not None:
        print prev_word + " count is "+ str(counts)


prev_word = None
counts = 0

for line in sys.stdin:
    word, value = line.split('\t',1)
    if word != prev_word:
        wcount(prev_word, counts)
        prev_word = word
        counts = 0

    counts += eval(value)

wcount(prev_word, counts)
