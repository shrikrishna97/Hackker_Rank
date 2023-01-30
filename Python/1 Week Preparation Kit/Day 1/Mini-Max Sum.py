#!/bin/python3

import math
import os
import random
import re
import sys

'''Given five positive integers, 
find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example
arr = [1,3,5,7,9]
The minimum sum is 1+3+5+7=16 and the maximum sum is 3+5+7+9=24. 
The function prints

16 24 '''

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    mini=0
    maxi=0
    l = []
    arr.sort()
    for i in range(len(arr)):
        
        n=0
        for j in range(len(arr)-1):
            n+=arr[j]
        arr.reverse()    
        l.append(n)    
    print(min(l),max(l))    
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
