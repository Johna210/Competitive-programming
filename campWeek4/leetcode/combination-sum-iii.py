class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = set()
        def backtrack(path,idx,path_sum):
            if len(path) == k:
                if path_sum == n:
                    sorted_path = sorted(path)
                    ans.add(tuple(sorted_path))
                return
            for choice in range(idx,10):
                path.append(choice)
                backtrack(path,choice+1,path_sum + path[-1])
                path.pop()

        backtrack([],1,0)

        return ans