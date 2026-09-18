from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = defaultdict(int)
        for ch in magazine:
            dic[ch] += 1

        for ch in ransomNote:
            if ch not in dic or dic[ch] == 0:
                return False
            else:
                dic[ch] -= 1

        return True
        