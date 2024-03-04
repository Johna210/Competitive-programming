class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROWS,COLS = len(matrix), len(matrix[0])
        sub_matrix_sum = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                top = sub_matrix_sum[r-1][c] if r > 0 else 0
                left = sub_matrix_sum[r][c-1] if c > 0 else 0
                top_left = sub_matrix_sum[r-1][c-1] if min(r,c) > 0 else 0
                sub_matrix_sum[r][c] = matrix[r][c] + left + top - top_left

        ans = 0
        for r1 in range(ROWS):
            for r2 in range(r1,ROWS):
                counts = defaultdict(int)
                counts[0] = 1
                for c in range(COLS):
                    curr_sum = sub_matrix_sum[r2][c] - (
                        sub_matrix_sum[r1-1][c] if r1 > 0 else 0
                        )
                    diff = curr_sum - target
                    ans += counts[diff]
                    counts[curr_sum] += 1
        return ans