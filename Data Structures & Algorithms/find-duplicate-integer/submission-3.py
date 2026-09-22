class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        found = [False] * n
        for num in nums:
            if not found[num]:
                found[num] = True
            else:
                return num