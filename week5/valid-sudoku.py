class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subgrid = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

                if i <= 2:
                    if j <= 2:
                        if board[i][j] in subgrid[0]:
                            return False
                        subgrid[0].add(board[i][j])
                    elif j <= 5:
                        if board[i][j] in subgrid[1]:
                            return False
                        subgrid[1].add(board[i][j])
                    else:
                        if board[i][j] in subgrid[2]:
                            return False
                        subgrid[2].add(board[i][j])

                elif i <= 5:
                    if j <= 2:
                        if board[i][j] in subgrid[3]:
                            return False
                        subgrid[3].add(board[i][j])
                    elif j <= 5:
                        if board[i][j] in subgrid[4]:
                            return False
                        subgrid[4].add(board[i][j])
                    else:
                        if board[i][j] in subgrid[5]:
                            return False
                        subgrid[5].add(board[i][j])
                else:
                    if j <= 2:
                        if board[i][j] in subgrid[6]:
                            return False
                        subgrid[6].add(board[i][j])
                    elif j <= 5:
                        if board[i][j] in subgrid[7]:
                            return False
                        subgrid[7].add(board[i][j])
                    else:
                        if board[i][j] in subgrid[8]:
                            return False
                        subgrid[8].add(board[i][j])

        for i in range(len(board)):
            col = 0
            seen = set()
            while col < len(board):
                if board[col][i] in seen:
                    return False
                if board[col][i] == ".":
                    col+=1
                    continue
                seen.add(board[col][i])
                col+=1

        return True

