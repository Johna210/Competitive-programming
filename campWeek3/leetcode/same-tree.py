# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(p,q):
            if p and q and p.val == q.val:
                left = traverse(p.left,q.left)
                right = traverse(p.right,q.right)
                return left and right
            elif not p and not q:
                return True
            elif not p or not q:
                return False
            

        return traverse(p,q)


            