# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        l1_int = 0
        cnt = 0
        while node is not None:
            l1_int += node.val * (10 ** cnt)
            cnt += 1
            node = node.next

        node = l2
        l2_int = 0
        cnt = 0
        while node is not None:
            l2_int += node.val * (10 ** cnt)
            cnt += 1
            node = node.next

        nodes_int = l1_int + l2_int
        digit = nodes_int % 10  # Get the last digit
        nodes_int //= 10  # Remove the last digit
        node = ListNode(val=digit)
        head = node
        while nodes_int > 0:
            digit = nodes_int % 10  # Get the last digit
            nodes_int //= 10  # Remove the last digit
            node.next = ListNode(val=digit)
            node = node.next
        return head