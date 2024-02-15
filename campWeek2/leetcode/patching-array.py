class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        patches, pref = 0, 0
        i = 0
        while pref < n:
            if i < len(nums) and nums[i] <= pref + 1:
                pref += nums[i]
                i += 1
            else:
                pref += (pref + 1)
                patches += 1
        return patches