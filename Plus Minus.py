#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    d1=0
    d2=0
    d3=0
    n1=0
    n2=0
    n3=0
    p=0
    n=0
    z=0
    li=[]
    for i in arr:
        if(i>0):
            p+=1
        elif(i<0):
            n+=1
        else:
            z+=1
    d1=p/len(arr)
    n1=round(d1,6)
    d2=n/len(arr)
    n2=round(d2,6)
    d3=z/len(arr)
    n3=round(d3,6)
    li.append(n1)
    li.append(n2)
    li.append(n3)
    for i in li:
        print(i)
    print()
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
