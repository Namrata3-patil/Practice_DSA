def plusMinus(arr):
    # Write your code here
    pos=neg=ze=0
    n=len(arr)
    for num in arr:
        if num>0:
            pos+=1
        elif num==0:
            ze+=1
        elif num<0:
            neg+=1
    print(f"{pos/n:.6f}")
    print(f"{neg/n:.6f}")
    print(f"{ze/n:.6f}")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
'''
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive: , negative:  and zeros: .
'''
