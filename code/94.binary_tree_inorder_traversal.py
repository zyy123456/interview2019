# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, s = [], []
        p = root
        while p or len(s) != 0:
            while p:
                s.append(p)
                p = p.left
            p = s.pop()
            res.append(p.val)
            p = p.right
        return res
