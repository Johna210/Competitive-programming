class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        majority = len(nums) // 3
        output = []

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

            if counts[num] > majority and num not in output:
                    output.append(num)
        
        if counts[nums[-1]] > majority and nums[-1] not in output:
            output.append(nums[-1])
        return output