class MinStack:

    def __init__(self):
        self.stack = []
        self.dp = [float('inf')]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.dp.append(min(self.dp[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.dp.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.dp[-1]
