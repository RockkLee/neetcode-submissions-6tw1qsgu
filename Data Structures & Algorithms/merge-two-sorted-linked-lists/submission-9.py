# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        node = ListNode()
        head = node
        while node1 and node2:
            temp1 = node1.next
            temp2 = node2.next
            if node1.val <= node2.val:
                node.next = node1
                node = node1
                node1 = temp1
            else:
                node.next = node2
                node = node2
                node2 = temp2
        if node1:
            node.next = node1
        if node2:
            node.next = node2
        return head.next

