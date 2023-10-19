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
    value = arr[-1]
    for i in range(n-1,-1,-1):
        if value > arr[i-1]:
            arr[i] = value
            print(*arr)
            break
        else:
            if i == 0:
                arr[i] = value
            else:
                arr[i] = arr[i-1]

        print(*arr)

# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     insertionSort1(n, arr)


num = 10
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

num2 = 5
arr2 = [2,4,6,8,3]

print(insertionSort1(num2,arr2))
print(insertionSort1(num,arr))
