class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minArray = len(nums) + 1
        current = 0

        for right in range(len(nums)):            
            current += nums[right]
            while current >= target:
                minArray = min(minArray,right-left+1)
                current -= nums[left]
                left+=1

        if minArray <= len(nums):
            return minArray
        else:
            return 0 
        