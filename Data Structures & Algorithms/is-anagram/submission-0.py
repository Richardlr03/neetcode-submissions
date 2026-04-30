from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for ch in s:
            dic[ch] += 1
        for ch in t:
            if dic[ch] == 0:
                return False
            else:
                dic[ch] -= 1
        for key in dic:
            if dic[key] != 0:
                return False
        return True

        