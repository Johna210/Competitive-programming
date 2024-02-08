class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]

        postfix = [0] * (len(nums) + 1)
        for i in range(len(nums)-1,-1,-1):
            postfix[i] = postfix[i+1] + nums[i]
        
        for i in range(len(nums)):
            if prefix[i] == postfix[i+1]:
                return i
        return -1