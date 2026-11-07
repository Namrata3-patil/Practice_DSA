#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    matching= {')': '(', ']': '[', '}': '{'}
    stack=[]
    for char in s:
        if char in matching.values():
            stack.append(char)
            
        elif char in matching.keys():
            if stack and stack[-1]==matching[char]:
                stack.pop()
            else:
                return "NO"
        else:
            return "NO"
            
    return "YES" if not stack else "NO"
                
    # Balanced only if all opened brackets are successfully matched and popped

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
'''
Sample Input

STDIN           Function
-----           --------
3               n = 3
{[()]}          first s = '{[()]}'
{[(])}          second s = '{[(])}'
{{[[(())]]}}    third s ='{{[[(())]]}}'
Sample Output

YES
NO
YES
'''
