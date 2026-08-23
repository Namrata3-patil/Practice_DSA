# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    # Step 1: Create the new node
    new_node = SinglyLinkedListNode(data)
    
    # Step 2: If inserting at the very beginning (position 0)
    if position == 0:
        new_node.next = llist
        return new_node
    
    # Step 3: Traverse to the node just before the target position
    current = llist
    for _ in range(position - 1):
        current = current.next
        
    # Step 4: Insert the new node and fix pointers
    new_node.next = current.next
    current.next = new_node
    
    return llist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
