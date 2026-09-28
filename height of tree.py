''''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if root is None:
        return -1 # Base case: empty tree has height 0
    
    # Add 1 for the current node
    return max(height(root.left), height(root.right)) + 1





tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))

'''
Success
Input (stdin)
7
3 5 2 1 4 6 7
Expected Output
''''
