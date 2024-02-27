class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(curr):
            if len(curr) == len(nums):
                # print(f"output {ans}")
                ans.append(curr[:])
                return
            for c in range(len(nums)):
                if nums[c] not in curr:
                    curr.append(nums[c])
                    backtrack(curr)
                    curr.pop()

        backtrack([])
        return ans