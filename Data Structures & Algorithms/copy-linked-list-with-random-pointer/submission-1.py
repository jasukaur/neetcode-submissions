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

        curr = head

        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        dummy = Node(0)
        org = head
        curr = oldToNew[org]
        dummy.next = curr
        

        while curr:
            curr.next = oldToNew[org.next]
            curr.random = oldToNew[org.random]

            curr = curr.next
            org =org.next
        
        return dummy.next
