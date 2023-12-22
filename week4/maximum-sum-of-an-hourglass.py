class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        output = 0
        i = 0
        j = 0

        while i <= len(grid) - 3:
            while j <= len(grid[0]) - 3:
                curr_sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] +grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                output = max(curr_sum,output)
                j+=1
            i+=1
            j=0
        
        return output