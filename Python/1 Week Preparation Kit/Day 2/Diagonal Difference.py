#!/bin/python3

import math
import os
import random
import re
import sys

'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal =1+5+9=15 . The right to left diagonal 3+5+9=17 . 
Their absolute difference is |15-17|=2.
'''
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    su = 0
    nu = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                su += arr[i][j]
            if j ==len(arr)-1:    
                nu += arr[i][j-i]     
    return abs(nu-su)            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
