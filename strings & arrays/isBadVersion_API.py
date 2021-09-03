import math
import os
import random
import re
import sys

#
# Complete the 'isBadVersion' function below.
#
# The function is enpected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY versions
#  2. INTEGER version
#
def binarySearch(arr, h, l, n):
    if l<=h:
        m = (h + l)//2

        if arr[m] == n:
            return m
        
        if arr[m] > n:
            return binarySearch(arr, m-1, l, n)
        else:
            return binarySearch(arr, h, m+1, n)
    else:
        return -1


def isBadVersion(versions, version):
    # Write your code here
 
    index = binarySearch(versions, len(versions)-1, 0, version)
    
    return index


if __name__ == '__main__':


    input_versions_array = list(map(int, input().rstrip().split()))

    input_version = int(input().strip())

    bad = isBadVersion(input_versions_array, input_version)

    print (bad)

