class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:   
        n = len(nums)
        op = 0
        right = n - 1
        left = right - 1
        left_pointer = nums[left] 
        right_pointer = nums[right]

        while left >= 0:
            if left_pointer > right_pointer:
                spaces = math.ceil(left_pointer / right_pointer)
                left_pointer = left_pointer // spaces
                op+=spaces-1
            right_pointer = left_pointer
            left-=1
            left_pointer = nums[left]

        return op
