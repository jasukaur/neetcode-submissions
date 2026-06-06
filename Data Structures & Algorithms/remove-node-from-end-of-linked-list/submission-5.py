# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        j = head
        dummy = ListNode(0, head)
        while n>0:
            j = j.next
            n -= 1
        i = dummy
        while j:
            j = j.next
            i = i.next
        
        i.next = i.next.next
        return dummy.next