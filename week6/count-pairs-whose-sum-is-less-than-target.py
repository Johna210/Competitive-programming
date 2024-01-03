class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        output = 0

        left = 0

        while left < len(nums):
            for right in range(left+1,len(nums)):
                if nums[left] + nums[right] < target:
                    output+=1
            left+=1
        return output                
            