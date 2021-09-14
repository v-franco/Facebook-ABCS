import math
import os
import random
import re
import sys

#
# Complete the 'string_permutations' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY alphabet
#  2. INTEGER permutation_length
#

def string_permutations(alphabet, permutation_length):
    # Write your code here
    if len(alphabet) == 1:
        return alphabet
    
    def recursivePermutations(alphabet, permutation_length, length, perm):
        if permutation_length == 0:
            print(perm)
            return

        for i in range(length):
            newPerm = perm + alphabet[i]
            recursivePermutations(alphabet, permutation_length-1, length, newPerm)

    recursivePermutations(alphabet, permutation_length, len(alphabet), "")

        

if __name__ == '__main__':

    alphabet_input = input().rstrip().split()

    permutation_length_input = int(input().strip())

    string_permutations(alphabet_input, permutation_length_input)