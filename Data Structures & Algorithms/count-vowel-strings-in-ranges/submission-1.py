class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for w in words:
            if w[0] in "aeiou" and w[-1] in "aeiou":
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])

        ans = []
        for q in queries:
            l, r = q
            ans.append(prefix[r+1] - prefix[l])

        return ans
        