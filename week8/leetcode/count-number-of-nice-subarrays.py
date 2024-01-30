class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        subarray_count = 0
        odd_count = 0

        for right in range(len(nums)):
            if nums[right]%2 != 0:
                odd_count += 1
                count = 0

            if odd_count == k:
                while left < len(nums) and nums[left] % 2 ==0:
                    count+=1
                    left += 1

                count += 1
                odd_count -= 1
                left += 1
            subarray_count += count
        return subarray_count

            