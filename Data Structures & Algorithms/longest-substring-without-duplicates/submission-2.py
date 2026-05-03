class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = 0
        j = 0
        n = len(s)
        visited = set()

        while j < n:
            if s[j] not in visited:
                visited.add(s[j])
                j += 1
            else:
                ans = max(ans, j - i)
                while i < n and s[i] != s[j]:
                    visited.remove(s[i])
                    i += 1
                i += 1
                j += 1
        ans = max(ans, j-i)

        return ans