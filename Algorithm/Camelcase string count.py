def camelcase(s):
    # Write your code here
    count=0
    for i in s:
        if ord(i)<=90 and ord(i)>=65:
            count=count+1
    return count+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
  '''
  Sample Input

saveChangesInTheEditor
Sample Output

5
Explanation

String  contains five words:

save
Changes
In
The
Editor
'''
