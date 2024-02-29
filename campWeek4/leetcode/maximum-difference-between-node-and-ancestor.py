# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = float("-inf")
        def find(node):
            nonlocal max_diff
            if not node:
                return (float("inf"),float("-inf")) 

            left_min, left_max = find(node.left)  
            right_min, right_max = find(node.right)
            mins = min(left_min,right_min)
            maxs = max(left_max, right_max)
            val = max(node.val-mins,maxs-node.val)
            max_diff = max(max_diff, val)
            return min(node.val, left_min, right_min), max(node.val, left_max, right_max)
        find(root)
        return max_diff