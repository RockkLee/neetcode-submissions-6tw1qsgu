# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.val is not None and head.next is None:
            return None
        if n == 1:
            node = head
            while node.next.next is not None:
                node = node.next
            node.next = None
            return head
        cnt = 0
        pre_slow_n = head
        slow_n = head
        fast_n = head
        while fast_n.next is not None:
            if cnt == n - 1:
                pre_slow_n = slow_n
                slow_n = slow_n.next
            else:
                cnt += 1
            fast_n = fast_n.next

        if pre_slow_n == slow_n:
            return slow_n.next
        pre_slow_n.next = slow_n.next
        return head
