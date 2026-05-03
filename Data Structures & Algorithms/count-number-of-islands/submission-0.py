class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    ans += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        visited.add((x, y))
                        if x > 0 and grid[x-1][y] == "1" and (x-1, y) not in visited:
                            stack.append((x-1, y))
                        if x < m - 1 and grid[x+1][y] == "1" and (x+1, y) not in visited:
                            stack.append((x+1, y))
                        if y > 0 and grid[x][y-1] == "1" and (x, y-1) not in visited:
                            stack.append((x, y-1))
                        if y < n - 1 and grid[x][y+1] == "1" and (x, y+1) not in visited:
                            stack.append((x, y+1))

        return ans