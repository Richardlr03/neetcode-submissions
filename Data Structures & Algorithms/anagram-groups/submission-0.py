from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            dic[ss].append(s)

        ans = []
        for key in dic:
            ans.append(dic[key])

        return ans

        