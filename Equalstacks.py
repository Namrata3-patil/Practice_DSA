def equalStacks(h1, h2, h3):
    # Write your code here
    sum1, sum2, sum3 = sum(h1), sum(h2), sum(h3)
    i, j, k = 0, 0, 0
    
    while sum1 != sum2 or sum2 != sum3:
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= h1[i]
            i += 1
        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= h2[j]
            j += 1
        elif sum3 >= sum1 and sum3 >= sum2:
            sum3 -= h3[k]
            k += 1
            
    return sum1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
'''
Sample Input

STDIN       Function
-----       --------
5 3 4       h1[] size n1 = 5, h2[] size n2 = 3, h3[] size n3 = 4  
3 2 1 1 1   h1 = [3, 2, 1, 1, 1]
4 3 2       h2 = [4, 3, 2]
1 1 4 1     h3 = [1, 1, 4, 1]
Sample Output

5
'''
