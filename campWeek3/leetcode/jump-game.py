class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = len(nums) - 1
        right = len(nums) - 2

        while right >= 0:
            if nums[right] + right >= good:
                good = right
            right-=1

        return good == 0
    