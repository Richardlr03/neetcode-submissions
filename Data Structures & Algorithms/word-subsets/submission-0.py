from collections import defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dic = defaultdict(int)
        for word in words2:
            dic_word = defaultdict(int)
            for ch in word:
                dic_word[ch] += 1
                dic[ch] = max(dic[ch], dic_word[ch])

        ans = []
        for word in words1:
            d = defaultdict(int)
            for ch in word:
                d[ch] += 1
            for key in dic:
                if key not in d or dic[key] > d[key]:
                    break
            else:
                ans.append(word)

        return ans
