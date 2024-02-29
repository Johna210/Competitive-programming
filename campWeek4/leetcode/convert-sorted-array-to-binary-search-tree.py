# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBST(node,nums):
            if nums:
                mid = len(nums) // 2
                node.val = nums[mid]
                node.left = makeBST(TreeNode(),nums[:mid])
                node.right = makeBST(TreeNode(),nums[mid+1:])

                return node 

        return makeBST(TreeNode(),nums)