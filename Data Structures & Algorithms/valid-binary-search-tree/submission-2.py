# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        order = []

        def inorder(node):
            if node.left:
                inorder(node.left)
            order.append(node)
            if node.right:
                inorder(node.right)

        inorder(root)
        n = len(order)
        for i in range(n-1):
            if order[i].val >= order[i+1].val:
                return False
        return True

        