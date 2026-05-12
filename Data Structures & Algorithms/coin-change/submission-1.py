class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount + 1)
        for i in range(amount+1):
            flag = False
            for c in coins:
                if i == c:
                    dp[i] = 1
                    flag = True
                elif i > c and dp[i-c]:
                    dp[i] = min(dp[i], 1 + dp[i-c])
                    flag = True
            if not flag:
                dp[i] = 0


        if not dp[-1]:
            return -1
        return dp[-1]

        