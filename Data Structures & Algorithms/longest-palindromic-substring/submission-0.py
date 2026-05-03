class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
            ch = s[i]
            left = i - 1
            right = i + 1
            while left >= 0 and s[left] == ch:
                left -= 1
            while right < n and s[right] == ch:
                right += 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            cur = s[left+1:right]
            if len(ans) < len(cur):
                ans = cur

        return ans