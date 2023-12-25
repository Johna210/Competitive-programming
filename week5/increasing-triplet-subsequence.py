class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = max(nums) 
        for num in nums: 
            if num <= first: 
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
            
        