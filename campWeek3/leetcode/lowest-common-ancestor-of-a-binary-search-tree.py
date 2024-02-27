# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root,p,q):
            if p.val > root.val and q.val > root.val:
                return find(root.right,p,q)
            elif p.val < root.val and q.val < root.val:
                return find(root.left,p,q)
            else:
                return root

        return find(root,p,q)