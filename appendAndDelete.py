#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    firstStart = True
    
    if len(s) + len(t) < k:
        # Iterate till the beginning of s
        while k > 0:
            if k <= len(t):
                s = s + t[len(s):len(s)+1]
            else:
                s = s[:-1]
            k -= 1            
            #print(k, s)
    else:
        # Iterate till the first occurance of the stripped part of s 
        while k > 0:
            subS = t[:len(s)]
            if not firstStart and subS == s and len(t)-len(s) >= k and (len(t)-len(s)-k)%2 == 0:
                s = s + t[len(s):len(s)+1]
            else:
                s = s[:-1]
            k -= 1
            firstStart = False
            #print(k, s)

    return 'Yes' if s == t and k == 0 else 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
