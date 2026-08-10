class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        square = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in row[i]:
                        return False
                    else:
                        row[i].add(board[i][j])
                    
                    if board[i][j] in column[j]:
                        return False
                    else:
                        column[j].add(board[i][j])
                    
                    Sindex = (3*(i//3))+(j//3)
                    if board[i][j] in square[Sindex]:
                        return False
                    else:
                        square[Sindex].add(board[i][j])

        return True