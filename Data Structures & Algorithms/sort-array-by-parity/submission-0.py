from collections import deque

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        q = deque()
        for num in nums:
            if num%2==0:
                q.appendleft(num)
            else:
                q.append(num)

        return list(q)
        