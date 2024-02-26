# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node,left,right):
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            a = validate(node.left,left,node.val)
            b = validate(node.right,node.val,right)
            return a and b

        return validate(root,float("-inf"),float("inf"))

