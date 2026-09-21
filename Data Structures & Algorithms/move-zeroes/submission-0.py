class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        count = 0
        while count < n:
            if nums[i] == 0:
                i -= 1
            else:
                num = nums[i]
                for j in range(i-1, -1, -1):
                    nums[j+1] = nums[j]
                nums[0] = num
            count += 1

        return nums
        