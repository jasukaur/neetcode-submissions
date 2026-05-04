class ListNode:

    def __init__(self, key=None, value = None):
        self.key = key
        self.val = value
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity
        
    def add(self, node):
        temp = self.left.next
        self.left.next, node.prev = node, self.left
        temp.prev = node
        node.next = temp


    def remove(self, node):
        prevNode =node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.add(self.cache[key])
        
        return self.cache[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = ListNode(key= key, value=value)
        self.add(node)
        self.cache[key] = node

        if len(self.cache)> self.capacity:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]
        
