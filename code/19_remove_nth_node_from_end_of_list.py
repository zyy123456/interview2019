# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next: return None
        pre, cur = head, head
        for _ in range(n):
            cur = cur.next
        if not cur:
            return head.next
        
        while cur.next:
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next
            
        return head
