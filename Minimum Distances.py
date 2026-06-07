#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    li=[]
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if(a[i]-a[j])==0:
                cal=abs(i-j)
                li.append(cal)
    if(len(li)==0):
        return -1
    else:
        return min(li)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
