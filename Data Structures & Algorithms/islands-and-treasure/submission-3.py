LAND = 2147483647


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dq: deque[Tuple[int, int]] = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dq.append((r, c))

        def add(r: int, c: int):
            if (0 <= r < ROWS and 0 <= c < COLS and
                    grid[r][c] == LAND and (r, c) not in dq):
                dq.append((r, c))

        dist = 0
        while dq:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
                grid[r][c] = dist
            dist += 1
