class MinStack:

    def __init__(self):
        self.stack: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        if len(self.stack) > 0:
            _, minn = self.stack[-1]
            self.stack.append((val, min(val, minn)))
            return
        self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        val, _ = self.stack[-1]
        return val

    def getMin(self) -> int:
        _, minn = self.stack[-1]
        return minn
