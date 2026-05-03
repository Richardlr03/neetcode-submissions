class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        m = len(heights)
        n = len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        for i in range(n):
            stack = [(0, i)]
            while stack:
                x, y  = stack.pop()
                pacific[x][y] = True
                if x < m - 1 and heights[x][y] <= heights[x+1][y] and not pacific[x+1][y]:
                    stack.append((x+1, y))
                if y < n - 1 and heights[x][y] <= heights[x][y+1] and not pacific[x][y+1]:
                    stack.append((x, y+1))
                if x > 0 and heights[x][y] <= heights[x-1][y] and not pacific[x-1][y]:
                    stack.append((x-1, y))
                if y > 0 and heights[x][y] <= heights[x][y-1] and not pacific[x][y-1]:
                    stack.append((x, y-1))

        for i in range(m):
            stack = [(i, 0)]
            while stack:
                x, y  = stack.pop()
                pacific[x][y] = True
                if x < m - 1 and heights[x][y] <= heights[x+1][y] and not pacific[x+1][y]:
                    stack.append((x+1, y))
                if y < n - 1 and heights[x][y] <= heights[x][y+1] and not pacific[x][y+1]:
                    stack.append((x, y+1))
                if x > 0 and heights[x][y] <= heights[x-1][y] and not pacific[x-1][y]:
                    stack.append((x-1, y))
                if y > 0 and heights[x][y] <= heights[x][y-1] and not pacific[x][y-1]:
                    stack.append((x, y-1))

        for i in range(n-1, -1, -1):
            stack = [(m-1, i)]
            while stack:
                x, y  = stack.pop()
                atlantic[x][y] = True
                if x < m - 1 and heights[x][y] <= heights[x+1][y] and not atlantic[x+1][y]:
                    stack.append((x+1, y))
                if y < n - 1 and heights[x][y] <= heights[x][y+1] and not atlantic[x][y+1]:
                    stack.append((x, y+1))
                if x > 0 and heights[x][y] <= heights[x-1][y] and not atlantic[x-1][y]:
                    stack.append((x-1, y))
                if y > 0 and heights[x][y] <= heights[x][y-1] and not atlantic[x][y-1]:
                    stack.append((x, y-1))

        for i in range(m-1, -1, -1):
            stack = [(i, n-1)]
            while stack:
                x, y  = stack.pop()
                atlantic[x][y] = True
                if x < m - 1 and heights[x][y] <= heights[x+1][y] and not atlantic[x+1][y]:
                    stack.append((x+1, y))
                if y < n - 1 and heights[x][y] <= heights[x][y+1] and not atlantic[x][y+1]:
                    stack.append((x, y+1))
                if x > 0 and heights[x][y] <= heights[x-1][y] and not atlantic[x-1][y]:
                    stack.append((x-1, y))
                if y > 0 and heights[x][y] <= heights[x][y-1] and not atlantic[x][y-1]:
                    stack.append((x, y-1))

        # print(pacific)
        # print(atlantic)

        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])

        return ans

