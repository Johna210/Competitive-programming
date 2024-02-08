class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0 
        prefix_sum = 0
        prefix = defaultdict(int)
        prefix[0] = 1

        for num in nums:
            prefix_sum = prefix_sum + num
            if prefix_sum - k in prefix:
                result += prefix[prefix_sum - k]
            prefix[prefix_sum] += 1

        return result

       
