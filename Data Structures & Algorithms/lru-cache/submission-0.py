class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.capacity = capacity
        self.size = 0
        self.dummy = Node()
        self.MRU = self.dummy

    def get(self, key: int) -> int:
        if key in self.keys:
            if self.keys[key] is self.MRU:
                return self.MRU.val
            
            next_node = self.keys[key].next
            prev_node = self.keys[key].prev
            next_node.prev = self.keys[key].prev
            prev_node.next = self.keys[key].next
            self.keys[key].next = None
            self.keys[key].prev = self.MRU
            self.MRU.next = self.keys[key]
            self.MRU = self.MRU.next
            return self.keys[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].val = value
            if self.keys[key] is not self.MRU:
                current = self.keys[key]
                current.next.prev = current.prev
                current.prev.next = current.next
                current.next = None
                current.prev = self.MRU
                self.MRU.next = current
                self.MRU = self.MRU.next

        elif self.size < self.capacity:
            self.MRU.next = Node(key, value)
            self.MRU.next.prev = self.MRU 
            self.MRU = self.MRU.next
            self.keys[key] = self.MRU
            self.size+=1
        else:
            if self.capacity == 1:
                self.keys.pop(self.dummy.next.key)
                self.dummy.next = Node(key, value)
                self.dummy.next.prev = self.dummy
                self.MRU = self.dummy.next
                self.keys[key] = self.MRU
            else:
                LRU = self.dummy.next
                LRU.next.prev = LRU.prev
                self.dummy.next = LRU.next
                LRU.next = None
                LRU.prev = None
                self.keys.pop(LRU.key)
                self.MRU.next = Node(key, value)
                self.MRU.next.prev = self.MRU
                self.MRU = self.MRU.next
                self.keys[key] = self.MRU

        
