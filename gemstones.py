#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    counter = 0
    gem_counter = 0
    for letter in letters:
        for el in arr:
            if letter not in el:
                break
            else:
                counter += 1
                
        if counter == len(arr):
            gem_counter += 1
        counter = 0
            
    return gem_counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
