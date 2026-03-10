#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    minimum=0
    maximum=0
    for i in range(0,4):
        minimum+=arr[i]
    for i in range(1,5):
        maximum+=arr[i]
    print(str(minimum) + " " + str(maximum))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
