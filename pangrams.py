#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lis = list(set(s.lower()))
    lis.sort()
    if ' ' in lis:
        lis.remove(' ')
    new_string = ''.join(lis)
    
    if new_string == alphabet:
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
