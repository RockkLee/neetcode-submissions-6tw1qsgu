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
        dic: Dict[Node|None, Node|None] = {None:None}
        node = head
        while node is not None:
            dic[node] = Node(x=node.val)
            node = node.next

        node = head
        while node is not None:
            dic[node].next = dic[node.next]
            dic[node].random = dic[node.random]
            node = node.next

        return dic[head]