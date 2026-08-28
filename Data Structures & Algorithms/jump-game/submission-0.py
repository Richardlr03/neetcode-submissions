class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = n - 1
        goal = n - 1
        while i>=0:
            target = goal - nums[i]
            if target <= i:
                goal = i
            i -= 1

        return goal == 0
        