
import math
import os
import random
import re
import sys

#
# Complete the 'find_unique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY haystack as parameter.
#


def find_unique(haystack):
    # Write your code here
    hsCounter = {}

    for key in haystack:

        if key not in hsCounter:
            hsCounter[key] = 1
        else:   
            hsCounter[key] += 1

    for key in haystack:

        if hsCounter[key] == 1:
            return key
        
    return -1



if __name__ == '__main__':


    input_haystack = list(map(int, input().rstrip().split()))

    unique_number = find_unique(input_haystack)

    print (unique_number)