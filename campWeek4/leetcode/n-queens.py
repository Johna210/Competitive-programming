class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited = set()
        vis_cols = set()
        ans = []
        def backtrack(row,avoid_d_1,avoid_d_2,avoid_c,path):
            if len(path) >= n:
                if len(path) == n:
                    ans.append(path[:])
                return
            
            for i in range(n):
                if i in avoid_c:
                    continue
                if (row-i) in avoid_d_1:
                    continue
                if (i+row) in avoid_d_2:
                    continue
                s = ["."] * n
                s[i] = 'Q'
                path.append(s)

                avoid_c.add(i)
                avoid_d_1.add(row-i)
                avoid_d_2.add(row+i)

                backtrack(row+1,avoid_d_1,avoid_d_2,avoid_c,path)

                avoid_c.remove(i)
                avoid_d_1.remove(row-i)
                avoid_d_2.remove(row+i)

                path.pop()
        
        backtrack(0,vis_cols,visited,set(),[])
        for a in ans:
            for i in range(len(a)):
                a[i] = "".join(a[i])

        return ans

