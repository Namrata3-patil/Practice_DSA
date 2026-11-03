#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
        stack = []
    max_stack = []
    res = []
    
    for op in operations:
        parts = op.split()
        q_type = int(parts[0])
        
        if q_type == 1:
            val = int(parts[1])
            stack.append(val)
            if not max_stack:
                max_stack.append(val)
            else:
                max_stack.append(max(val, max_stack[-1]))
        elif q_type == 2:
            if stack:
                stack.pop()
                max_stack.pop()
        elif q_type == 3:
            if max_stack:
                res.append(max_stack[-1])
                
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
