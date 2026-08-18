# PROBLEM: Insert a new node with given data at the tail (end) of a singly linked list.
# SOLUTION: Handle empty list by making the new node the head; otherwise, traverse 
#           to the end of the list and link the last node's 'next' pointer to the new node.

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    # 1. Create the new node with the given data
    new_node = SinglyLinkedListNode(data)

    # 2. If the list is empty, the new node becomes the head
    if head is None:
        return new_node

    # 3. Otherwise, traverse to the last node
    current = head
    while current.next is not None:
        current = current.next

    # 4. Link the last node's next pointer to the new node
    current.next = new_node

    # 5. Return the original head of the list
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
