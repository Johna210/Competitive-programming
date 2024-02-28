class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(path):
            if sum(path) >= target:
                if sum(path) == target:
                    sorted_path = sorted(path)
                    if sorted_path not in ans:
                        ans.append(sorted_path)
                return
            for choice in range(len(candidates)):
                path.append(candidates[choice])
                backtrack(path)
                path.pop()

        backtrack([])

        return ans
