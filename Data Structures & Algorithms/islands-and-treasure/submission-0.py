class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def chk_and_append(dq: deque, pos_m: int, pos_n: int, steps: int):
            if grid[pos_m][pos_n] == -1:
                return
            if grid[pos_m][pos_n] == 0:  # tressure is found
                return
            if steps != 2147483647 and steps > grid[pos_m][pos_n]:  # no need to do bfs
                return
            grid[pos_m][pos_n] = steps
            dq.append((pos_m, pos_n, steps))
            return

        def bfs(m: int, n: int):
            dq: deque[Tuple[int, int, int]] = deque()
            dq.append((m, n, 0))
            while dq:
                pos_m, pos_n, steps = dq.popleft()
                if pos_m != 0:
                    chk_and_append(dq, pos_m - 1, pos_n, steps + 1)
                if pos_m != len(grid) - 1:
                    chk_and_append(dq, pos_m + 1, pos_n, steps + 1)
                if pos_n != 0:
                    chk_and_append(dq, pos_m, pos_n - 1, steps + 1)
                if pos_n != len(grid[0]) - 1:
                    chk_and_append(dq, pos_m, pos_n + 1, steps + 1)

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 0:
                    bfs(m, n)
