class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        m = len(heights)
        n = len(heights[0])

        for i in range(m):
            for j in range(n):
                visited = set()
                stack = [(i, j)]
                pacific = False
                atlantic = False
                while stack:
                    x, y = stack.pop()
                    visited.add((x, y))
                    if x == 0 or y == 0:
                        pacific = True
                    if x == m - 1 or y == n - 1:
                        atlantic = True
                    if x < m - 1 and heights[x][y] >= heights[x+1][y] and (x+1, y) not in visited:
                        stack.append((x+1, y))
                    if x > 0 and heights[x][y] >= heights[x-1][y] and (x-1, y) not in visited:
                        stack.append((x-1, y))
                    if y < n - 1 and heights[x][y] >= heights[x][y+1] and (x, y+1) not in visited:
                        stack.append((x, y+1))
                    if y > 0 and heights[x][y] >= heights[x][y-1] and (x, y-1) not in visited:
                        stack.append((x, y-1))

                if pacific and atlantic:
                    ans.append([i, j])

        return ans

