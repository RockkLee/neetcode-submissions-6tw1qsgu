# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        node = head
        while node:
            node = node.next
            cnt += 1
        if cnt == 0:
            return
        
        pre, node = None, head
        for _ in range(cnt - n):
            pre = node
            node = node.next
        if pre:
            pre.next = node.next
        if node == head:
            head = head.next if head else None
        else:
            node = None
        return head
        
