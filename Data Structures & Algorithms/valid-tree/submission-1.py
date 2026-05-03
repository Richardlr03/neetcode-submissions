from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = set()

        stack = [0]
        while stack:
            u = stack.pop()
            count = 0
            visited.add(u)
            for v in g[u]:
                if v not in visited:
                    stack.append(v)
                else:
                    count += 1
            if count > 1:
                return False

        if len(visited) != n:
            return False
        return True

        