class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_index = 0

        for i in range(len(flips)):
            max_index = max(flips[i],max_index)
            if max_index == i + 1:
                count+=1

        return count