class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        nodes: [ListNode] = deque()
        while node is not None:
            nodes.append(node)
            node = node.next

        joint: ListNode | None = None
        while len(nodes) > 0:
            if len(nodes) == 1:
                if not joint:  # the len of the nodes are equal to 1
                    break
                joint.next = nodes.pop()
                joint.next.next = None
                break
            first = nodes.popleft()
            last = nodes.pop()
            first.next = last
            last.next = None
            if joint:
                joint.next = first
            joint = last
