class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        hash_nums = {}

        for i in range(len(nums)):
            hash_nums[nums[i]] = i

        for index,val in operations:
            nums[hash_nums[index]] = val
            hash_nums[val] =hash_nums[index]

        return nums


