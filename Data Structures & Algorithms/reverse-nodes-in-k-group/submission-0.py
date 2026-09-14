# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        c = head
        start = head
        end = head
        old_end = None

        while c: # need to recheck conditiom
            counter = 1
            while counter < k:
                if start.next:
                    start = start.next
                    counter+=1
                else:
                    old_end.next = end
                    return head
            
            if old_end:
                old_end.next = start
            else:
                head = start
            
            prev = None

            while prev != start:
                n = c.next
                c.next = prev
                prev = c
                c = n
            old_end = end
            end = c
            start = end

        return head




