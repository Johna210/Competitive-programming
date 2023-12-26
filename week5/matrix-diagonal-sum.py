class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat[0])
        i = 0
        j = 0
        
        primary_diagonal = 0
        secondary_diagonal = 0
        while i < len(mat[0]) and n > 0:
            left_most = [i,i]
            right_most = [j,n-1]
            
            primary_diagonal += mat[left_most[0]][left_most[1]]
            secondary_diagonal += mat[right_most[0]][right_most[1]]
            
            print(primary_diagonal)
            print(f"secondary - {secondary_diagonal}")

            i+=1
            j+=1
            n-=1

        if len(mat) % 2 == 0:
            return primary_diagonal + secondary_diagonal
            
        return primary_diagonal + secondary_diagonal - (mat[len(mat)//2][len(mat[0])//2])