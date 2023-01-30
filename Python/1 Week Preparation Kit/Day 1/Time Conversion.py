#!/bin/python3

import math
import os
import random
import re
import sys
'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example:
s='12:01:00PM'
Return '12:01:00'.

s='12:01:00AM'
Return '00:01:00'.
'''
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    c=12
    if s[0:2]=="12" and s[-2]=="A":
        s2="00"
        s2 = s2 + s[2:-2] 
        return s2   
    if s[-2]=="P":
        if s[0:2]=="12":
            c=c
        else:    
            c = c+int(s[0:2])
        s1 = s[2:-2]
        s1 = str(c) + s1
        return s1
    else:
        return s[:-2]        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
