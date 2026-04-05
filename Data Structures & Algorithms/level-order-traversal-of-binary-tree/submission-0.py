# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        res: List[List[int]] = []
        dq: deque[Tuple[TreeNode, int]] = deque()
        dq.append((root, 0))

        while len(dq) >0:
            node, idx = dq.popleft()
            if node.left is not None:
                dq.append((node.left, idx + 1))
            if node.right is not None:
                dq.append((node.right, idx + 1))

            if idx > len(res) - 1:
                res.append([node.val])
            else:
                res[idx].append(node.val)

        return res
        