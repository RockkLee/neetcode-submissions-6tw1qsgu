# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 0, 1, 2, 3
#    s     f

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec_half = slow.next
        pre, node = None, sec_half
        slow.next = None
        while node:
            temp = node.next
            node.next = pre
            pre = node
            node = temp

        front = head
        rear = pre

        while front and rear:
            temp1 = front.next
            temp2 = rear.next
            front.next = rear
            rear.next = temp1
            front = temp1
            rear = temp2

            
