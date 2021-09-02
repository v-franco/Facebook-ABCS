import math
import os
import random
import re
import sys

#
# Complete the 'merge_arrays' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr1
#  2. INTEGER_ARRAY arr2
#

#manually sort the arrays
def insertionSort(arr):

    for i in range (1, len(arr)):
        curVal = arr[i]
        pos = i

        while ((pos > 0) and (arr[pos-1] > curVal)):
            arr[pos] = arr[pos-1]
            pos -= 1

        arr[pos] = curVal

    return arr


def merge_arrays(arr1, arr2):
    # Write your code here
    merged = insertionSort(arr1 + arr2)

    return merged
    
    
if __name__ == '__main__':


    arr1_in_count = int(input().strip())

    arr1_in = list(map(int, input().rstrip().split()))

    arr2_in_count = int(input().strip())

    arr2_in = list(map(int, input().rstrip().split()))

    ret = merge_arrays(arr1_in, arr2_in)

    print(ret)