# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = defaultdict(list)
        def traverse(node,idx,level):
            if not node:
                return
            output[idx].append((level,node.val))
            traverse(node.left,idx-1,level+1)
            traverse(node.right,idx+1,level+1)
        traverse(root,0,0)
        min_index = float("inf") 
        max_index = float("-inf")
        for arr in output:
            min_index = min(arr,min_index)
            max_index = max(arr,max_index)
            output[arr].sort()
        index = min_index
        res = []
        while index <= max_index:
            temp = []
            for i in range(len(output[index])):
                temp.append(output[index][i][1])
            res.append(temp)
            index+=1
        return res