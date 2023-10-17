#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    value = arr[-1]
    arr[-1] = arr[-2]
    for i in range(len(arr)-1,0,-1):
        if arr[i] > n:
            arr[i] = arr[i-1]
        else:
            arr[i] = value
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)