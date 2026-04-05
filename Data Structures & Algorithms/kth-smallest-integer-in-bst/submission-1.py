# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Use Inorder DFS to get the elements from the smallest to the largest
        """

        cnt = 0

        def inorder(node: TreeNode) -> int | None:
            nonlocal cnt
            if node is None:
                return None

            # left traversal
            lval = inorder(node.left)
            if lval is not None:
                return lval
            # take action
            cnt += 1
            if cnt == k: return node.val
            # right traversal
            rval = inorder(node.right)
            if rval is not None:
                return rval

            return None

        return inorder(root)