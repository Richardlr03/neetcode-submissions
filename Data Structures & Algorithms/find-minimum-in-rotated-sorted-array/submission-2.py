class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        if n == 1:
            return nums[0]

        while i < j:
            if i + 1 == j:
                return min(nums[i], nums[j])
            mid = (i+j)//2
            if nums[i] < nums[j]:
                j = mid
            elif nums[mid] > nums[i] and nums[mid] > nums[j]:
                i = mid
            else:
                j = mid
    
        