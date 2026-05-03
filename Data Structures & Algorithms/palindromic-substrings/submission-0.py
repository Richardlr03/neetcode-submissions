class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        i = 0

        while i < n:
            ch = s[i]
            left = i - 1
            right = i + 1
            count = 1
            while right < n and s[right] == ch:
                count += 1
                right += 1
            idx = right
            ans += count * (count + 1) // 2
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
            i = idx

        return ans
         