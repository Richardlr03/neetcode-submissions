# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        order = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            order.append(node.val)
            inorder(node.right)

        inorder(root)
        ans = float('inf')
        n = len(order)
        for i in range(n-1):
            ans = min(ans, order[i+1] - order[i])

        return ans
        