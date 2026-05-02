class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        ans = ""
        for i in range(n):
            ans += str(len(strs[i])) + "#" + strs[i]
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        i = 0
        cur = ""
        num = True
        cur_num = ""
        while i < n:
            if num:
                cur_num = ""
                while s[i] != "#":
                    cur_num += s[i]
                    i += 1
                cur_num = int(cur_num)
                i += 1
                num = False
            else:
                cur_word = ""
                for j in range(cur_num):
                    cur_word += s[i]
                    i += 1
                ans.append(cur_word)
                num = True
        if cur_num == 0:
            ans.append("")

        return ans