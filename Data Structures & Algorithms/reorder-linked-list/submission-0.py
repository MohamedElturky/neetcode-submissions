# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = head
        tail = head

        while tail and tail.next:
            mid=mid.next
            tail = tail.next.next

        c = mid.next
        mid.next = None
        p = None

        while c:
            n = c.next
            c.next = p
            p = c
            c = n

        start = head
        while p:
            n = start.next
            np = p.next
            start.next = p
            p.next = n
            start = n
            p = np

        

