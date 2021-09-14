import math
import os
import random
import re
import sys

#
# Complete the 'find_max' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY array_of_integers as parameter.
#

def find_max(array_of_integers):
    # Write your code here
    if len(array_of_integers) == 2:
        if array_of_integers[0] < array_of_integers[1]:
            return array_of_integers[1]
        else:
            return array_of_integers[0]
    
    else:
        return find_max([array_of_integers[0], find_max(array_of_integers[1:])])

    

if __name__ == '__main__':

    input_array_of_integers = list(map(int, input().rstrip().split()))

    max_val = find_max(input_array_of_integers)

    print (max_val)

