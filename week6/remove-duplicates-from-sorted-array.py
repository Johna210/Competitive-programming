class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # seen = []
        # left = 0
        # right = 1

        # if len(nums) == 1:
        #     return 1

        # while right < len(nums):
        #     if nums[left] not in seen:
        #         seen.append(nums[left])
        #         left += 1
        #     if nums[right] not in seen:
        #         nums[left] = nums[right]
        #     else:
        #         right += 1
        
        # return left

        right = 1
        for left in range(1,len(nums)):
            if nums[left] != nums[left-1]:
                nums[right] = nums[left]
                right+=1
        return right