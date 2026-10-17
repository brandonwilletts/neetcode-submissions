class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.next: Node = None
        self.prev: Node = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)

        # Link head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.use(key)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.use(key)
            return
        
        self.cache[key] = Node(key, value)
        self.insert(key)
        
        if len(self.cache) > self.capacity:
            self.evict()

    def insert(self, key: int):
        node = self.cache[key]
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def use(self, key: int):
        node = self.cache[key]

        # Remove node
        node.prev.next = node.next
        node.next.prev = node.prev

        # Insert node at tail
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
    
    def evict(self):
        key = self.head.next.key
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        del self.cache[key]
