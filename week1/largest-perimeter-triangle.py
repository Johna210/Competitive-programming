class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        max_perimeter = 0

        nums.sort()
        left = 0
        right = len(nums) - 1
        while left >= 0:
            if nums[right] < (nums[right-1] + nums[right-2]):
                max_perimeter = max(max_perimeter,nums[right]+nums[right-1]+nums[right-2])
                break
            right-=1
            left = right - 2

        return max_perimeter