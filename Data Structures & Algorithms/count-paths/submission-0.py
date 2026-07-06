# leetcode 62
from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1

        seen = set()
        dq = deque()
        dq.append((0, 0))

        while dq:
            pos_m, pos_n = dq.popleft()

            if (pos_m, pos_n) in seen:
                continue

            # Move down
            if pos_m + 1 < m:
                grid[pos_m + 1][pos_n] += grid[pos_m][pos_n]
                dq.append((pos_m + 1, pos_n))

            # Move right
            if pos_n + 1 < n:
                grid[pos_m][pos_n + 1] += grid[pos_m][pos_n]
                dq.append((pos_m, pos_n + 1))

            seen.add((pos_m, pos_n))

        return grid[m - 1][n - 1]