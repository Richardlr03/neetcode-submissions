class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n-1

        while i <= j:
            mid = (i+j)//2
            num = nums[mid]
            if num > target:
                if num < nums[i]:
                    j = mid - 1
                elif target >= nums[i]:
                    j = mid - 1
                else:
                    i = mid + 1
            elif num < target:
                if num > nums[j]:
                    i = mid + 1
                elif target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                return mid

        return -1
        