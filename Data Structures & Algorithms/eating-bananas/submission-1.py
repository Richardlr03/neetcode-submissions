import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = 10**13
        ans = 0

        while i <= j:
            mid = (i+j)//2
            cur = 0
            for p in piles:
                cur += math.ceil(p/mid)
            if cur <= h:
                ans = mid
                j = mid - 1
            else:
                i = mid + 1

        return ans

        