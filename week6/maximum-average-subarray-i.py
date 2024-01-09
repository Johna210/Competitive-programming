class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_subarray = sum(nums[:k])
        max_avg = curr_subarray / k
        for i in range(k,len(nums)):
            curr_subarray -= nums[i-k]
            curr_subarray += nums[i]

            avg = curr_subarray / k
            max_avg = max(avg,max_avg)
        return max_avg