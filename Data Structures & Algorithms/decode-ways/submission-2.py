class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] * (n+1)

        for i, ch in enumerate(s):
            if ch == "0":
                if s[i-1] != "1" and s[i-1] != "2":
                    return 0
                else:
                    dp[i+1] = dp[i-1]
            else:
                if i == 0:
                    dp[i+1] = dp[i]
                else:
                    dp[i+1] = dp[i]
                    if s[i-1] == "1":
                        dp[i+1] += dp[i-1]
                    elif s[i-1] == "2" and int(s[i]) <= 6:
                        dp[i+1] += dp[i-1]
        print(dp)
        return dp[-1]
        