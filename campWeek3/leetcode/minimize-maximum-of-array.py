class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_val = target = nums[0]

        if max(nums) == max_val :
            return max_val

        for i in range(1,len(nums)):
            target+=nums[i]
            max_val = max(math.ceil(target/(i+1)),max_val)

        return max_val
