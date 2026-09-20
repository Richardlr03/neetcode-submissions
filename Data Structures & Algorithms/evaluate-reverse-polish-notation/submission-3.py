import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch != "+" and ch != "-" and ch != "*" and ch != "/":
                stack.append(ch)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if ch == "+":
                    ans = b+a
                elif ch == "-":
                    ans = b-a
                elif ch == "*":
                    ans = b*a
                else:
                    ans = math.trunc(b/a)
                stack.append(ans)
        return int(stack[0])
        