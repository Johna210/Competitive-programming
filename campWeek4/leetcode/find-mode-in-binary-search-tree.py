# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = defaultdict(int)
        max_count = 0
        def count(node):
            nonlocal max_count
            if not node:
                return
            counts[node.val] += 1
            max_count = max(max_count,counts[node.val])
            count(node.left)
            count(node.right)
        count(root)
        output = []
        for count in counts:
            if counts[count] == max_count:
                output.append(count)
        return output
