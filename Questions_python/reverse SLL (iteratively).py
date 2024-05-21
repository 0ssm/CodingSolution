class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def reverse(head):
    if head is None or head.next is None:
        return head
    prev = head
    curr = prev.next
    next = curr.next
    prev.next = None
    while next:
        curr.next = prev
        prev = curr
        curr = next
        next = next.next
    curr.next = prev
    return curr

