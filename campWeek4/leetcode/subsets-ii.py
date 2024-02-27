class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def func(curr,path):
            if len(path) == len(nums):
                return
            
            for idx in range(curr,len(nums)):
                path.append(nums[idx])
                if sorted(path) not in ans:
                    ans.append(sorted(path[:]))

                func(idx+1,path)
                path.pop()

        ans = []
        func(0,[])
        return [[]] + ans