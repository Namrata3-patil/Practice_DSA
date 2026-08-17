# PROBLEM: Find the maximum value in an array of size 'n' (initially all zeros)
# after performing 'm' operations that add 'k' to all elements between indices 'a' and 'b'.
# SOLUTION: Uses a Difference Array (Prefix Sum) approach to optimize updates to O(1).
# Instead of iterating through the range [a, b], we mark +k at index 'a' and -k at 'b+1'.
# A single final pass computes the running prefix sum to find the global maximum in O(n) time.

import math
import os
import random
import re
import sys

# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    arr = [0] * (n + 2)
    
    # Mark the start and end of each range
    for a, b, k in queries:
        arr[a] += k
        if b + 1 <= n:
            arr[b + 1] -= k
            
    # Find the maximum value using a running sum
    max_val = 0
    current_sum = 0
    for i in range(1, n + 1):
        current_sum += arr[i]
        if current_sum > max_val:
            max_val = current_sum
            
    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
