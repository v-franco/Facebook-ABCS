import math
import os
import random
import re
import sys

#
# Complete the 'sum_to_one' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING digits as parameter.
#

def sum_to_one(digits):
    # Write your code here
    if digits == "":
        return 0    

    temp = int(int(digits[0]) + int(sum_to_one(digits[1:]))) 

    if temp > 10:
        return sum_to_one(str(temp))
    else:
        return temp
        


if __name__ == '__main__':

    input_string = input()

    single_digit_sum = sum_to_one(input_string)

    print(single_digit_sum)
