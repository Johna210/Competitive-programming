# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def check(root, sums):
            nonlocal max_sum
            if not root:
                max_sum = max(max_sum, 0)
                return (float("inf"), float("-inf"), 0, True)

            left = check(root.left, sums)
            right = check(root.right, sums)

            if left[3] and right[3] and left[1] < root.val < right[0]:
                value = left[2] + right[2] + root.val
                max_sum = max(max_sum, value)
                return (min(root.val, left[0]), max(root.val, right[1]), value, True)

            return (0,0,0, False)

        check(root, 0)
        return max_sum