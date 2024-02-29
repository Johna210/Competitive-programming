# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(lst):
            if not lst:
                return
            # slicing array and create a new node
            max_val = max(lst)
            index = lst.index(max_val)
            left_side = (lst[:index])
            right_side = (lst[index+1:])
            # recursively add left and ride side
            node = TreeNode(max_val)
            node.left = build_tree(left_side)
            node.right = build_tree(right_side)
            return node    

        return build_tree(nums)
