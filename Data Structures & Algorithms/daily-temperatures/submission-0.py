from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dq = deque()
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            if len(dq) == 0 or dq[-1][0] >= temp:
                dq.append((temp, idx))
            else:
                while len(dq) > 0:
                    if dq[-1][0] >= temp:
                        break
                    tup = dq.pop()
                    res[tup[1]] = idx - tup[1]
                dq.append((temp, idx))

        return res
