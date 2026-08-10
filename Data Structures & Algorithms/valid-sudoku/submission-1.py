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
                    Sindex = (3*(i//3))+(j//3)
                    if (board[i][j] in row[i]) or (board[i][j] in column[j]) or (board[i][j] in square[Sindex]):
                        return False
                    row[i].add(board[i][j])
                    column[j].add(board[i][j])
                    square[Sindex].add(board[i][j])
                    
                    

        return True