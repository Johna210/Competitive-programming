# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left,right):
            if not left and not right:
                return True

            elif (not left and right) or (not right and left) or left.val != right.val:
                return False
            first = check(left.left,right.right)
            second = check(left.right,right.left)
            return first and second
        return check(root,root) 

