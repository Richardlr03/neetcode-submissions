class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(dp[i-1], nums[i])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
        