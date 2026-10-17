def miniMaxSum(arr):
    # Sort the array in ascending order
    ar = sorted(arr)
    
    min_sum = 0
    max_sum = 0
    
    # Sum the first 4 elements for the minimum sum
    for i in range(4):
        min_sum += ar[i]
        
    # Sum the last 4 elements for the maximum sum
    for i in range(1, 5):
        max_sum += ar[i]
        
    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
'''
Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are , , , , and . Calculate the following sums using four of the five integers:

Sum everything except 1, the sum is .14
Sum everything except 5, the sum is .10
'''
