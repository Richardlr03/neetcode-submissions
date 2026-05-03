from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = set()
        ans = 0

        for i in range(n):
            if i not in visited:
                stack = [i]
                while stack:
                    u = stack.pop()
                    visited.add(u)
                    for v in g[u]:
                        if v not in visited:
                            stack.append(v)
                ans += 1

        return ans
        