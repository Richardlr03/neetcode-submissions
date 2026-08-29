class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        cur = []

        def backtrack(i):
            if sum(cur) == target:
                ans.append(cur.copy())
                return
            if sum(cur) > target:
                return
            for idx in range(i, len(nums)):
                cur.append(nums[idx])
                backtrack(idx)
                cur.pop()

        backtrack(0)
        return ans
        