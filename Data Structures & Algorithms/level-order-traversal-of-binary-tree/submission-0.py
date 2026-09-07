# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        if root:
            q.append((root, 0))
            cur = []
            cur_lvl = 0

            while q:
                node, lvl = q.popleft()
                if lvl == cur_lvl:
                    cur.append(node.val)
                else:
                    ans.append(cur)
                    cur = []
                    cur_lvl = lvl
                    cur.append(node.val)
                if node.left:
                    q.append((node.left, lvl+1))
                if node.right:
                    q.append((node.right, lvl+1))

            ans.append(cur)

        return ans

        