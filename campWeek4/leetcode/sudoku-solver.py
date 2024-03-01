class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def findBoxs(i,j):
            if i<3:
                if j < 3:
                    return '1'
                elif j < 6:
                    return '2'
                else:
                    return '3'
            elif i<6:
                if j < 3:
                    return '4'
                elif j < 6:
                    return '5'
                else:
                    return "6"
            else:
                if j < 3:
                    return '7'
                elif j < 6:
                    return '8'
                else:
                    return '9'

        cols = defaultdict(set)
        rows = defaultdict(set)
        local = defaultdict(set)

        points = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    loc = findBoxs(i,j)
                    local[loc].add(board[i][j])
                else:
                    points += 1

        def backtrack(row , column):
            if row == 9:
                return  True
            if column == 9:
                return backtrack(row + 1 ,0)

            if board[row][column] == '.':
                for value in range(1 ,10):
                    value = str(value)
                    if value in cols[column]:
                        continue
                    if value in rows[row]:
                        continue

                    current_box = findBoxs(row , column)
                    
                    if value in local[current_box]:
                        continue
                    
                    board[row][column] = str(value)

                    cols[column].add(value)
                    rows[row].add(value)
                    local[current_box].add(value)

                    if backtrack(row , column + 1):
                        return True
                    
                    cols[column].remove(value)
                    rows[row].remove(value)
                    local[current_box].remove(value)

                    board[row][column] = '.'

                return False

            return backtrack(row , column + 1)

        backtrack(0 , 0)