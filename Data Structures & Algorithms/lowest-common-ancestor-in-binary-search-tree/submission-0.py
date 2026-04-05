# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    - The number of nodes in the tree is in the range [2, 105].
    - -109 <= Node.val <= 109
    - All Node.val are unique.
    - p != q
    - p and q will exist in the BST.
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        target: TreeNode | None = None
        total = 0

        def preorder(node: TreeNode, cnt: int) -> int:
            nonlocal total, target, p, q

            if node is None or total == 2:
                return cnt
            if node.val == p.val or node.val == q.val:
                cnt += 1
                total = cnt

            lcnt = preorder(node.left, cnt)
            rcnt = preorder(node.right, cnt)
            if cnt == 0 and lcnt == 2 and rcnt == 0:
                if target is None:
                    target = node.left
                return 2
            elif cnt == 0 and lcnt == 0 and rcnt == 2:
                if target is None:
                    target = node.right
                return 2
            elif cnt == 0 and lcnt == 1 and rcnt == 1:
                if target is None:
                    target = node
                return 2

            return max(lcnt, rcnt)

        if root.val == p.val or root.val == q.val:
            return root
        preorder(root, 0)
        return target