class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "}":"{", "]":"["}
        stack = []
        for p in s:
            if p not in dic:
                stack.append(p)
            elif not stack:
                return False
            elif stack.pop() != dic[p]:
                return False

        if len(stack) != 0:
            return False
        return True
        