class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        r = total_sum % p

        if r == 0:
            return 0

        prefix_sum = 0
        rightmost_rem = {0: -1}
        ans = len(nums)
        for i, v in enumerate(nums):

            prefix_sum = (prefix_sum + v) % p

            right = (prefix_sum - r) % p

            if right in rightmost_rem:
                j = rightmost_rem[right]
                ans = min(ans, i - j)
            rightmost_rem[prefix_sum] = i

        return ans if ans < len(nums) else -1