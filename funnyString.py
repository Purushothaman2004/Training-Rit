#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    value_list = []
    reverse_list = []
    for i in s:
        value_list.append(ord(i))
        reverse_list.insert(0, ord(i))

    answer = True

    for i in range(len(s)-1):
        if abs(value_list[i] - value_list[i+1]) != abs(reverse_list[i] - reverse_list[i+1]):
            answer = False
            break

    if answer:
        return 'Funny'
    else:
        return 'Not Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
