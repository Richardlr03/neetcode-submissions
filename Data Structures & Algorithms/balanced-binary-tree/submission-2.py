# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find_height(node):
            if not node:
                return 0
            return 1 + max(find_height(node.left), find_height(node.right))

        if not root:
            return True
        left = find_height(root.left)
        right = find_height(root.right)

        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        