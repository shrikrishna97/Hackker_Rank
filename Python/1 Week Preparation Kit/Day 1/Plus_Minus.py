#!/bin/python3

import math
import os
import random
import re
import sys

'''Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. 
The test cases are scaled to six decimal places, 
though answers with absolute error of up to  are acceptable.'''
'''Example
arr=[1,1,0,-1,-1]
There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5, 2/5 and 1/5. 
Results are printed as:

0.400000
0.400000
0.200000 '''
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    l = len(arr)
    p=0;n=0;z=0
    for i in arr:
        if i>0:
            p+=1
        if i<0:
            n+=1
        if i==0:
            z +=1
    print(p/l)
    print(n/l)
    print(z/l)                

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
