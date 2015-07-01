#!/usr/bin/env python
#-*- coding: ascii -*-
# example of program that calculates the total number of times each word has been tweeted.
import sys

# global dictionary
word_dict = dict()

# function to print dictionary
def print_dict(obj,wf):
    for key in sorted(obj.iterkeys()):
        wf.write( "{:<30} {}\n".format(key, obj[key]) )

# function to add words to dictionary
def add_to_dict(words):
    #iterate through words
    for word in words:
        # increment if word is present, else add new
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1;
        else:
            word_dict[word] = 1;

# main function
def main():
    # read file handler 
    read_filename = sys.argv[1]
    rf = open(read_filename, 'r')
    # read line from the file
    for line in rf:
        # remove whitespace
        line = line.strip()
        # split into words
        words = line.split()
        # iterate and add to dictionary
        add_to_dict(words)
    # print the dictionary
    write_filename = sys.argv[2]
    wf = open(write_filename, 'w')
    print_dict(word_dict, wf)

if __name__ == '__main__': 
    main()
