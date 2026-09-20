class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            a = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in a:
                        return False
                    else:
                        a.add(board[i][j])
        for i in range(9):
            a = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in a:
                        return False
                    else:
                        a.add(board[j][i])
        middles = [(1, 1), (1,4), (1,7), (4,4), (4,1), (4,7), (7,1), (7,4), (7,7)]
        dir = [(0,0), (0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,-1), (-1,1)]
        for i, j in middles:
            a = set()
            for x, y in dir:
                if board[i+x][j+y] != ".":
                    if board[i+x][j+y] in a:
                        return False
                    else:
                        a.add(board[i+x][j+y])

        return True

                    