class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_value = max(nums)
        count = nums.count(max_value)

        if count > 1:
            return (max_value - 1) * (max_value-1)
        else:
            output = 0
            for num in nums:
                if num == max_value:
                    continue
                output = max(output,(max_value-1)*(num-1))
        
        return output