class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                max_one = max(current,max_one)
                current = 0
        
        return max(max_one,current)