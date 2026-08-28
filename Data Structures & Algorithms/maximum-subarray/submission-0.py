class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        cur = 0
        flag = False
        for num in nums:
            if num >= 0:
                flag = True
                cur = max(0, cur) + num
            else:
                ans = max(ans, cur)
                cur += num

        ans = max(ans, cur)
        if not flag:
            ans = max(nums)

        return ans