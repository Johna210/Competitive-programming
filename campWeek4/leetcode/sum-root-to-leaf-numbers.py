# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = 0
        def sumTree(root,num):
            nonlocal nums
            if not root:
                return 
            if (not root.left) and (not root.right):
                num += str(root.val)
                nums+=int(num)

            left = sumTree(root.left,num+str(root.val))
            right = sumTree(root.right,num+str(root.val))
           
        sumTree(root,"")
        return nums


