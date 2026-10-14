from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] != 0:
            return -1

        q = deque([(0, 0, 1)])
        dir = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        visited = set()

        while q:
            x, y, step = q.popleft()
            visited.add((x, y))
            if x == n-1 and y == n-1:
                return step
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny] == 0:
                    q.append((nx, ny, step+1))

        return -1
            
        