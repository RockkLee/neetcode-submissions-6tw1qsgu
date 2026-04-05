class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def chk_and_append(dq: deque, pos_m: int, pos_n: int):
            if grid[pos_m][pos_n] == 1:
                grid[pos_m][pos_n] = 2
                dq.append((pos_m, pos_n))

        def bfs(m: int, n: int) -> int:
            area = 0
            dq: deque[Tuple[int, int]] = deque()
            dq.append((m, n))
            while dq:
                pos = dq.popleft()
                pos_m, pos_n = pos[0], pos[1]
                area += 1
                grid[pos_m][pos_n] = 2
                if pos_m != 0:
                    chk_and_append(dq, pos_m - 1, pos_n)
                if pos_m != len(grid) - 1:
                    chk_and_append(dq, pos_m + 1, pos_n)
                if pos_n != 0:
                    chk_and_append(dq, pos_m, pos_n - 1)
                if pos_n != len(grid[0]) - 1:
                    chk_and_append(dq, pos_m, pos_n + 1)
            return area

        max_area = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    max_area = max(max_area, bfs(m, n))
        return max_area
