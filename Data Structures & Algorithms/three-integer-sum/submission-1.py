class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            cur = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                cur_sum = cur + nums[j] + nums[k]
                if cur_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    if nums[j] == nums[k]:
                        break
                    cur_j = nums[j]
                    cur_k = nums[k]
                    while nums[j] == cur_j:
                        j += 1
                    k -= 1
                    while nums[k] == cur_k:
                        k -= 1
                elif cur_sum < 0:
                    j += 1
                else:
                    k -= 1

        return ans
        