class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * (n+1)
        right = [1] * (n+1)
        for i in range(n):
            left[i+1] = left[i] * nums[i]
        for i in range(n-1, -1, -1):
            right[i] = right[i+1] * nums[i]

        ans = []
        for i in range(n):
            ans.append(left[i] * right[i+1])

        return ans
        