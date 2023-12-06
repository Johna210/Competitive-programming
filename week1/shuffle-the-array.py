class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_array = []

        for i in range(len(nums)//2):
            new_array.append(nums[i])
            new_array.append(nums[i+n])

        return new_array