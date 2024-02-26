# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def sums(root,total):
            if not root:
                return total
            elif root.val > high:
                total = sums(root.left,total)
            elif root.val < low:
                total = sums(root.right,total)
            elif low <= root.val <= high:
                total += root.val
                total = sums(root.left,total)
                total = sums(root.right,total)
            return total


        return sums(root,0)