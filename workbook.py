#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    page = 0
    special_problems = 0
    for i in range(n):
        exercises = arr[i]
        for j in range(1, exercises+1, 1):
            if k != 1:
                if j % k == 1:
                    page += 1
                if j == page:
                    special_problems += 1
            else:
                page +=1
                if j == page:
                    special_problems += 1
    return special_problems

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
