def pre_order(root):
  if root is None:
    return
  print(root.data, end="\t")
  pre_order(root.left)
  pre_order(root.right)


def in_order(root):
  if root is None:
    return
  in_order(root.left)
  print(root.data, end="\t")
  in_order(root.right)


def post_order(root):
  if root is None:
    return
  post_order(root.left)
  post_order(root.right)
  print(root.data, end="\t")
  '''
  preorder
  1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
Sample Output

1 2 5 3 4 6 
postorder
1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
Sample Output

1 2 5 3 4 6 
Inorder

Sample Input

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
Sample Output

1 2 3 4 5 6 """
