class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        temp = n
        if n < 0:
            temp *= -1
        count = 0
        while temp > 1:
            temp //= 2
            count += 1

        ans = x
        if n < 0:
            ans = 1/ans
        for i in range(count):
            ans **= 2

        temp = n
        if n < 0:
            temp *= -1

        rem = temp - 2 ** count
        if n > 0:
            ans *= x ** rem
        else:
            ans *= (1/x) ** rem

        return ans
        