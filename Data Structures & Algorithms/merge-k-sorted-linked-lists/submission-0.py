# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        new_lists = []
        if n == 0:
            return None
        if n == 1:
            return lists[0]

        for i in range(0, n, 2):
            if i == n - 1:
                new_lists.append(lists[i])
            else:
                head = ListNode()
                point = head
                while lists[i] and lists[i+1]:
                    if lists[i].val < lists[i+1].val:
                        point.next = lists[i]
                        lists[i] = lists[i].next
                        point = point.next
                    else:
                        point.next = lists[i+1]
                        lists[i+1] = lists[i+1].next
                        point = point.next

                if lists[i]:
                    point.next = lists[i]
                    new_lists.append(head.next)
                else:
                    point.next = lists[i+1]
                    new_lists.append(head.next)

        return self.mergeKLists(new_lists)

        
        