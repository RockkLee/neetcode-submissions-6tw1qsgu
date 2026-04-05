# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        dq: deque[Tuple[TreeNode, int]] = deque()
        dq.append((root, 0))

        res: List[int] = []
        while len(dq) > 0:
            node, layer = dq.popleft()
            if layer == len(res):
                res.append(node.val)
            else:
                res[layer] = node.val
            if node.left:
                dq.append((node.left, layer + 1))
            if node.right:
                dq.append((node.right, layer + 1))

        return res
        