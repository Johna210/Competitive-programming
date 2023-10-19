class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for i in nums:
            counts[i] += 1

        counter = 0
        j = 0
        while counter < len(counts):
            if counts[counter] == 0:
                counter += 1
            else:
                nums[j] = counter
                counts[counter] -= 1
                j += 1
