class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()
        def backtrack(path,idx,prev_sums):
            if prev_sums >= target:
                if prev_sums == target:
                    ans.add(tuple(path))
                return
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(path,i+1,prev_sums + path[-1])
                path.pop()

        backtrack([],0,0)

        return ans
