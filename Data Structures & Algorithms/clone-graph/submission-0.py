"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return None
        clones: dict[int, Node] = {}
        dq: deque['Node'] = deque()
        dq.append(root)
        clones[root.val] = Node(root.val)
        while dq:
            node = dq.popleft()
            for neighbor in node.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                    dq.append(neighbor)
                clones[node.val].neighbors.append(clones[neighbor.val])
        return clones[root.val]