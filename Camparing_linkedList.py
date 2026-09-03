#Compare the two linked lists and return 1 if the lists are equal. Otherwise, return 0. Do NOT print anything to stdout/console.
# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#

def compare_lists(llist1, llist2):
    # Loop until we reach the end of at least one list
    while llist1 is not None and llist2 is not None:
        # If the data values don't match, the lists are not equal
        if llist1.data != llist2.data:
            return 0
        
        # Move to the next nodes in both lists
        llist1 = llist1.next
        llist2 = llist2.next
        
    # If both lists reached None at the same time, they are identical in length and values
    if llist1 is None and llist2 is None:
        return 1
    
    # If one list was longer than the other
    return 0

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
