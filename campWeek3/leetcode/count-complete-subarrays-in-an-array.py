class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distincts = len(set(nums))
        counts = defaultdict(int)
        left = count = 0

        for right in range(n):
            counts[nums[right]] += 1

            while len(counts) == distincts:
                count += n - right
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                left += 1

        return count