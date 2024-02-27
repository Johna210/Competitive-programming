# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def traverse(root,idx):
            if not root:
                return
            if idx >= len(ans):
                ans.append([root.val])
            else:
                ans[idx].append(root.val)
            traverse(root.left,idx+1)
            traverse(root.right,idx+1)
        traverse(root,0)

        for i in range(len(ans)):
            if i%2!=0:
                ans[i].reverse()
        return ans