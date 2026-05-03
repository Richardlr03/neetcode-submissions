class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = 0
        cur_max = 0
        ans = 0
        first = True

        for price in prices:
            if first:
                cur_min = price
                cur_max = price
                first = False
            elif price < cur_min:
                ans = max(ans, cur_max - cur_min)
                cur_min = price
                cur_max = price
            elif price > cur_max:
                cur_max = price

        ans = max(ans, cur_max - cur_min)

        return ans

        