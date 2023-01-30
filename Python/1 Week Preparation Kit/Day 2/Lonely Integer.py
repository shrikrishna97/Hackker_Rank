#!/bin/python3

import math
import os
import random
import re
import sys

'''
Given an array of integers, where all elements but one occur twice, find the unique element.

Example
arr = [1,2,3,4,3,2,1]
The unique element is 4.

Function Description

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

int a[n]: an array of integers
Returns

int: the element that occurs only once
'''
#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    nw = a.copy()
    
    qw = []
    for i in a:
        if i not in qw:
            qw.append(i)
            nw.remove(i)
        elif i in qw:
            qw.remove(i)                         
    return(qw[0])    
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
