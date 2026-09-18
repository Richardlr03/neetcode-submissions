class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        seen = set()

        def dfs(i, j, idx):
            if idx == l:
                return True

            if i<0 or i>=m or j<0 or j>=n or (i, j) in seen or board[i][j] != word[idx]:
                return False

            seen.add((i, j))

            found = (
                dfs(i+1, j, idx+1) or 
                dfs(i-1, j, idx+1) or 
                dfs(i, j+1, idx+1) or 
                dfs(i, j-1, idx+1)
            )

            seen.remove((i, j))

            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
        