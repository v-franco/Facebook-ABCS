
import math
import os
import random
import re
import sys

#
# Complete the 'longest_common_prefix' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY strings as parameter.
#


def longest_common_prefix(strings):
        lcp = ""

        if len(strings) == 0:
            return lcp

        if len(strings) == 1:
            return strings[0]
        
        strings = sorted(strings)

        for i in range(len(strings[0])):
            
            if strings[0][i] == strings[-1][i]:
                lcp += strings[0][i]
            else:
                return lcp
        
        return lcp



if __name__ == '__main__':


    strings_in_count = int(input().strip())

    strings_in = input().split()

    ret = longest_common_prefix(strings_in)

    print (ret)


