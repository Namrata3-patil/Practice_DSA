 #Complete the 'reversePrint' function below.
#
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reversePrint(llist):
    # Write your code here
   
    # Write your code here
    if llist is None:
        return
    
    # Use an array to store the values during traversal
    nodes = []
    current = llist
    
    while current:
        nodes.append(current.data)
        current = current.next
        
    # Print the values in reverse order
    for data in reversed(nodes):
        print(data)


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)
