class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[:3])
        output = 0
    
        for left in range(len(nums)-2):
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                val = nums[left] + nums[mid] + nums[right]

                if val > target:
                    right -= 1
                else:
                    mid += 1

                if(abs(val-target) < abs(closest-target)):
                        closest = val

        return closest
