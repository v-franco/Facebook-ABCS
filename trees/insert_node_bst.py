import math
import os
import random
import re
import sys

class BstNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

#
# Complete the 'insert_into_binary_tree' function below.
#
# The function is expected to return a BstNode, the root node of the tree after insertion.
# The function accepts BstNode bst, the root of the binary search tree, if none, return the new root node.
# The function accepts INTEGER value as the value to insert. 

def insert_into_binary_tree(bst, value):
    # implement insert here
    if not bst:
        return BstNode(value)
    else:
        if bst.value == value:
            return bst
        if bst.value < value:
            bst.right = insert_into_binary_tree(bst.right, value)
        else:
            bst.left = insert_into_binary_tree(bst.left, value)
    return bst

if __name__ == '__main__':

    input_numbers = []

    input_numbers_count = int(input().strip())
    for _ in range(input_numbers_count):
        input_numbers_item = int(input().strip())
        input_numbers.append(input_numbers_item)
        
    bst = None
    for input_number in input_numbers:
        bst = insert_into_binary_tree(bst, input_number)
        
    def print_helper(bst):
        if not bst:
            return
        print_helper(bst.left)
        print(bst.value)
        print_helper(bst.right)
    print_helper(bst)
    