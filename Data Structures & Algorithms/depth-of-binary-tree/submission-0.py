# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lheight = height(node.left)
            rheight = height((node.right))
            return max(lheight, rheight) + 1

        return height(root)

        