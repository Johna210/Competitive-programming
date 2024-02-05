class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = left = curr = 0
        seen = defaultdict(int)

        for right in range(len(nums)):

            seen[nums[right]] += 1
            curr+=nums[right]

            while left < right and seen[nums[right]] > 1:
                seen[nums[left]] -= 1
                curr -= nums[left]
                left+=1
            score = max(score,curr)

        return score
