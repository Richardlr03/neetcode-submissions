from collections import deque
import math

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        count = 0
        
        q = deque([nums[0]])
        visited = set([0])

        while q:
            node = q.popleft()
            count += 1

            for i, num in enumerate(nums):
                if i not in visited and math.gcd(num, node) != 1:
                    visited.add(i)
                    q.append(num)

        return count == len(nums)