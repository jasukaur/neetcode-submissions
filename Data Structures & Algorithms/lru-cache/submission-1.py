class ListNode:
    def __init__(self,key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}

        self.left , self.right = ListNode(), ListNode()
        self.left.next , self.right.prev = self.right, self.left
        
        self.capacity = capacity

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    def add(self, node):
        temp = self.left.next

        self.left.next = node
        node.prev = self.left

        node.next = temp
        temp.prev = node

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1


    def put(self, key: int, value: int) -> None:

        if key in self.hm:
            self.remove(self.hm[key])
        
        node = ListNode(key, value)
        self.hm[key] = node
        self.add(node)

        if len(self.hm) > self.capacity:
            lru = self.right.prev
            self.remove(lru)
            del self.hm[lru.key]


