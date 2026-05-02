from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        arr = []
        for key in dic:
            arr.append((key, dic[key]))

        arr.sort(key=lambda x:-x[1])
        ans = []
        for i in range(k):
            ans.append(arr[i][0])

        return ans