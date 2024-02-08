class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        perm = [0] * n

        for request in requests:
            perm[request[0]] += 1
            if request[1] + 1 < n:
                perm[request[1] + 1] -=1
        
        total = 0
        for idx, val in enumerate(perm):
            total += val
            perm[idx] = total
        perm.sort()
        nums.sort()
        res = 0
        l, r = len(nums) - 1 , len(perm) - 1
        while r > -1:
            res += perm[r] * nums[l]
            l -= 1
            r -= 1
        return res % (10 ** 9 + 7)

       
        