from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        pre_req = [0] * numCourses

        for a, b in prerequisites:
            g[b].append(a)
            pre_req[a] += 1

        visited = set()
        for i in range(numCourses):
            if pre_req[i] == 0 and i not in visited:
                q = deque([i])
                while q:
                    u = q.popleft()
                    visited.add(u)
                    for v in g[u]:
                        pre_req[v] -= 1
                        if pre_req[v] == 0:
                            q.append(v)
        
        return len(visited) == numCourses
        