class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        outputs = set()
        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue  # Skip duplicates of the left element.
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                val = nums[left] + nums[mid] + nums[right]
                if val == 0:
                    value = (nums[left],nums[mid],nums[right])
                    outputs.add(value)
                    mid += 1
                    right -= 1
                    # Skip duplicates of the middle and right elements.
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1
                    

                elif val > 0:
                    right -= 1
                elif val < 0:
                    mid += 1
                else: 
                    break
            

        return list(outputs)