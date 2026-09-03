# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def isSame(a, b):
            print(a.val, b.val)
            if a.val != b.val:
                return False

            if a.left and a.right and b.left and b.right:
                return isSame(a.left, b.left) and isSame(a.right, b.right)
            elif a.left and not b.left:
                return False
            elif not a.left and b.left:
                return False
            elif a.right and not b.right:
                return False
            elif not a.right and b.right:
                return False
            elif a.left and b.left:
                return isSame(a.left, b.left)
            elif a.right and b.right:
                return isSame(a.right, b.right)
            else:
                return True

        if not p and not q:
            return True
        elif not p or not q:
            return False
        return isSame(p, q)
        