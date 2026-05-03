class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, (j-i) * min(heights[i], heights[j]))
        
        return ans
        