# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def preorder(node: TreeNode, minn: float, maxx: float) -> bool:
            if node is None:
                return True
            if not minn < node.val < maxx:
                return False
            lcheck = preorder(node.left, minn, node.val)
            if not lcheck:
                return False
            rcheck =preorder(node.right, node.val, maxx)
            if not rcheck:
                return False
            return True

        return preorder(root, float("-inf"), float("inf"))