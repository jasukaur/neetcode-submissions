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
        oldToNew = {None:None}
        node = head
        curr = Node(0)
        prev = curr

        while node:
            oldToNew[node] = Node(node.val)
            node = node.next

        node = head
        
        while node:
            curr.next = oldToNew[node]
            curr= curr.next
            curr.next = oldToNew[node.next]
            curr.random = oldToNew[node.random]
            node = node.next
        return prev.next
