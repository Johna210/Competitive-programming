#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    count = 0
    while True: 
        swapcounter = 0
        for i in range(len(a)-1):
            # If the previous number in the list is greater than the next swap them
            if a[i] > a[i+1]:
                tmp = a[i]
                a[i] = a[i+1]
                a[i+1] = tmp

                swapcounter = 1
                count += 1
        # If there is no swap then it means its already sorted     
        if swapcounter == 0:
            break

    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
