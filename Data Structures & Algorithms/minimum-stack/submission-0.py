class MinStack:
    def __init__(self):
        self.dq = deque()

    def push(self, val: int) -> None:
        if len(self.dq) == 0:
            self.dq.append((val, val))
        else:
            self.dq.append((min(self.dq[-1][0], val), val))

    def pop(self) -> None:
        self.dq.pop()

    def top(self) -> int:
        return self.dq[-1][1]

    def getMin(self) -> int:
        return self.dq[-1][0]
