class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        for i in range(n-1):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(dp[i-1], nums[i])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        dp2 = [0] * n
        for i in range(1, n):
            if i == 1:
                dp2[i] = nums[i]
            elif i == 2:
                dp2[i] = max(dp2[i-1], nums[i])
            else:
                dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])

        return max(dp[-2], dp2[-1])
        