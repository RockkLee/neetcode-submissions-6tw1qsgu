from collections import deque
from typing import List, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        def chk_and_append(dq: deque[Tuple[int, int]], pos_m: int, pos_n: int):
            if grid[pos_m][pos_n] == "1":
                grid[pos_m][pos_n] = "2"
                dq.append((pos_m, pos_n))

        def bfs(m: int, n: int):
            nonlocal cnt
            dq: deque[Tuple[int, int]] = deque()
            dq.append((m, n))
            while dq:
                pos = dq.popleft()
                pos_m, pos_n = pos[0], pos[1]
                grid[pos_m][pos_n] = "2"
                if pos_m != 0:
                    chk_and_append(dq, pos_m - 1, pos_n)
                if pos_m != len(grid) - 1:
                    chk_and_append(dq, pos_m + 1, pos_n)
                if pos_n != 0:
                    chk_and_append(dq, pos_m, pos_n - 1)
                if pos_n != len(grid[0]) - 1:
                    chk_and_append(dq, pos_m, pos_n + 1)
            cnt += 1

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                node = grid[m][n]
                if node == "1":
                    bfs(m, n)
        return cnt
