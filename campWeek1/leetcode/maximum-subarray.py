class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        max_value = prefix_sum[0]

        for i in range(1,len(nums)):
            curr = prefix_sum[i-1]
            if curr < 0:
                curr = 0

            prefix_sum[i] = curr + nums[i]
            max_value = max(max_value,prefix_sum[i])

        return max_value