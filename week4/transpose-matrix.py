class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = []
        index = 0
        i = len(matrix[0])
        while index < i:
            new = []
            for row in matrix:
                new.append(row[index])
            output.append(new)
            index+=1
        return output
            