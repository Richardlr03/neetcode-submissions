class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        n1 = len(s)
        n2 = len(t)

        while i<n1 and j<n2:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1

        return n2-j