def findMergeNode(head1, head2):
    # Step 1: Get the lengths of both lists
    def get_length(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    len1 = get_length(head1)
    len2 = get_length(head2)
    
    # Step 2: Align the pointers to be equidistant from the merge point
    current1 = head1
    current2 = head2
    
    if len1 > len2:
        for _ in range(len1 - len2):
            current1 = current1.next
    else:
        for _ in range(len2 - len1):
            current2 = current2.next
            
    # Step 3: Traverse together until the references match
    while current1 and current2:
        if current1 == current2:
            return current1.data
        current1 = current1.next
        current2 = current2.next
        
    return None
