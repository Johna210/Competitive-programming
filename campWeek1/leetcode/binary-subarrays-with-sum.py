class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        prefix_sum = 0
        output = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in prefix:
                output += prefix[prefix_sum-goal]
            prefix[prefix_sum] += 1

        return output

