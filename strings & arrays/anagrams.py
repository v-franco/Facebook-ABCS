
import math
import os
import random
import re
import sys

#
# Complete the 'are_anagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#
def bubbleSort(arr):
    for i in range (len(arr)):
        for j in range (len(arr) - 1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def are_anagrams(s1, s2):
    # Write your code here
    s1 = bubbleSort(list(s1))
    s2 = bubbleSort(list(s2))

    if (s1 == s2):
        return 1
    else:
        return 0
    

if __name__ == '__main__':

    s1_in = input()

    s2_in = input()

    val = are_anagrams(s1_in, s2_in)

    print (val)