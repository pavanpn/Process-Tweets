Insight Data Engineering - Coding Challenge
===========================================================
Submission by: Pavan Kumar Pavagada Nagaraja

## Summary
The two features given as a part of the coding challenege has been implemeted in Python. Please note that Feature #2 implementation uses 'Median Tracker' Python package to compute the running median.

## Usage Instructions
1. Install the Median Tracker package
    sudo python -m pip install MedianTracker
2. Run the shell script 'run.sh'

## Output of the 'tree' command:
    .
    ├── images
    │   └── directory-pic.png
    ├── README.md
    ├── run.sh
    ├── src
    │   ├── median_unique.py
    │   └── words_tweeted.py
    ├── tweet_input
    │   └── tweets.txt
    └── tweet_output
        ├── ft1.txt
        └── ft2.txt

## Sample Output

1. Calculate the total number of times each word has been tweeted.
    #analytics                     1
    #bigdata                       3
    #kdn                           1
    #smb                           1
    @cxotodayalerts                1
    @lavanyarathnam                1
    and                            1
    answer                         1
    astrazeneca                    1
    being                          1
    big                            2
    business.                      1
    businesses:                    1
    data                           1
    deployed                       1
    effective                      1
    end                            1
    finally                        1
    for                            2
    healthcare                     1
    how                            1
    http://bddy.me/1bzukb3         1
    http://ow.ly/o8gt3             1
    http://ow.ly/ot2uj             1
    interview:                     1
    is                             3
    just                           1
    not                            1
    of                             1
    on                             2
    poverty?                       1
    promise                        1
    small                          1
    the                            2
    to                             1
    wang,                          1
    xia                            1

2. Calculate the median number of *unique* words per tweet, and update this median as tweets come in. 
    11.00
    12.50
    14.00


Please contact me if you have any questions.
