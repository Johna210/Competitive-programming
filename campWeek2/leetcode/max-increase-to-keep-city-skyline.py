class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        col = row = len(grid)
        
        max_cols = [0] * col
        max_rows = [0] * row

        for i in range(row):
            max_rows[i] = max(grid[i])
            for j in range(col):
                max_cols[j] = max(max_cols[j],grid[i][j])
        total_sum = 0
        for i in range(row):
            for j in range(col):
                total_sum += grid[i][j] - max_rows[i] if max_rows[i] <= max_cols[j] else grid[i][j] - max_cols[j] 
        
        return abs(total_sum)