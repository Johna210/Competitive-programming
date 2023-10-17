class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hash_nums = {}

        for i in range(len(nums)):
            hash_nums[nums[i]] = i

        for operation in operations:
            index = hash_nums[operation[0]]
            nums[index] = operation[1]
            hash_nums[operation[1]] = index

        return nums
