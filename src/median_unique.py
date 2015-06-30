#!/usr/bin/env python
#-*- coding: ascii -*-
# example of program that calculates the median number of unique words per tweet.

import sys
import numpy as np
import heapq
from mediantracker import MedianTracker

# function to print dictionary
def print_median(running_median,wf):
    wf.write( '%.2f\n' % running_median ) 

# function to add words to dictionary
def count_unique_words(words):
    # global dictionary
    word_dict = dict()
    # count max unique elements 
    counter = 0
    # increase counters
    for word in words:
        # increase counter if unique word
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            counter += 1
    # return the number of unique words
    return counter

# main function
def main():
    # read file handler
    read_filename = sys.argv[1]
    rf = open(read_filename, 'r')
    # write file handler
    write_filename = sys.argv[2]
    wf = open(write_filename, 'w')
    # instantiate streaming median class
    tracker = MedianTracker()
    # read line from the file
    for line in rf:
        # remove whitespace
        line = line.strip()
        # split into words
        words = line.split()
        # iterate and add to dictionary
        counter = count_unique_words(words)
        # calculate running median
        tracker.add(counter) 
        running_median = (tracker.lower_median() + tracker.upper_median()) / 2.0   
        # write to file
        print_median(running_median,wf)

# go to main
if __name__ == '__main__': 
    main()
