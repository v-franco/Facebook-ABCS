import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def caesarCipherManual(s, k):
    # Write your code here
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    encryption=''

    for char in s:

        if char in uppercase:
            charIndex = uppercase.find(char)
            resultIndex = charIndex+k

            if resultIndex >= len(uppercase) or resultIndex < 0:
                resultIndex =- len(uppercase)

            encryption = encryption + uppercase[resultIndex]

        if char in lowercase:
            charIndex = lowercase.find(char)
            resultIndex = charIndex+k

            if resultIndex >= len(lowercase) or resultIndex < 0:
                resultIndex =- len(lowercase)

            encryption = encryption + lowercase[resultIndex]
            
        else:
            encryption = encryption + char
    
    return encryption

def caesarCipher(s, k):
    # Write your code here
    encryption=''

    for pos in range(len(s)):
        char = s[pos]
                        
        if not char.isalpha():
            encryption = encryption+char

        elif (char.isupper()):
            encryption += chr((ord(char)-65 + k) % 26 + 65)

        else:
            encryption += chr((ord(char)-97 + k) % 26 + 97)

    return encryption


if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)