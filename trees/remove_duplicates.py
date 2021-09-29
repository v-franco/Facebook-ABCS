#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
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

def removeDuplicates(llist):
    # Write your code here
    head = llist
    if head is None:
        return

    while head.next is not None:
        if head.data != head.next.data:
            head = head.next
        else:
            new_node = head.next.next
            head.next = None
            head.next = new_node

    return llist