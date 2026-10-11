#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Get the size of the square matrix
    n = len(arr)
    
    primary_sum = 0
    secondary_sum = 0
    
    for i in range(n):
        # Primary diagonal elements have matching row and column indices: (0,0), (1,1), (2,2)...
        primary_sum += arr[i][i]
        
        # Secondary diagonal elements track from opposite sides: (0, n-1), (1, n-2), (2, n-3)...
        secondary_sum += arr[i][n - 1 - i]
        
    # Return the absolute difference
    return abs(primary_sum - secondary_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
