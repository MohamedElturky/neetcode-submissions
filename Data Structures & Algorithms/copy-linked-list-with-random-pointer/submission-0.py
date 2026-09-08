"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        dic = {}
        old = head
        new = Node(old.val)
        head2 = new
        dic[old] = new

        while old.next:
            old = old.next
            new.next = Node(old.val)
            new = new.next
            dic[old] = new

        old = head
        new = head2

        while old:
            if old.random in dic:
                new.random = dic[old.random]
            else:
                new.random = None
            old = old.next
            new = new.next
        
        return head2
        