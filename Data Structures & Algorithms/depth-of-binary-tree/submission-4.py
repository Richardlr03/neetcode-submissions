# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def findMax(node, count):
            if not node:
                return count
            return max(findMax(node.left, count+1), findMax(node.right, count+1))
        return findMax(root, 0)
