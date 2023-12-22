class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        output = []
        index = {}

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i+j in index:
                    index[i+j].append(mat[i][j])
                else:
                    index[i+j] = [mat[i][j]]
        
        for item in index:
            if item % 2 != 0:
                output+=index[item]
            else:
                output+=index[item][::-1]
        
        return output
