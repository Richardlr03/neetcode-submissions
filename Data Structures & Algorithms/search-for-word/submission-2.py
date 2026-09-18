class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    stack = [(i, j, 0, set())]
                    while stack:
                        x, y, idx, seen = stack.pop()
                        if board[x][y] == word[idx]:
                            seen.add((x, y))
                            if idx == l-1:
                                return True
                            if x-1>=0 and (x-1, y) not in seen:
                                stack.append((x-1, y, idx+1, seen.copy()))
                            if x+1<m and (x+1, y) not in seen:
                                stack.append((x+1, y, idx+1, seen.copy()))
                            if y-1>=0 and (x, y-1) not in seen:
                                stack.append((x, y-1, idx+1, seen.copy()))
                            if y+1<n and (x, y+1) not in seen:
                                stack.append((x, y+1, idx+1, seen.copy()))

        return False
        