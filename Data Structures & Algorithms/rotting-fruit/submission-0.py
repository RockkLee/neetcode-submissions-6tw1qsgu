class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        if len(grid) == 1 and len(grid[0]) == 1:
            return -1 if grid[0][0] == 1 else 0

        def bfs(m: int, n: int):
            dq: deque[Tuple[int, int]] = deque()
            dq.append((m, n))
            seen: set[Tuple[int, int]] = set()
            while dq:
                row, col = dq.popleft()
                if row > 0 and grid[row - 1][col] != 0 and grid[row - 1][col] != 2 and grid[row - 1][col] not in seen:
                    if grid[row - 1][col] == 1 or grid[row - 1][col] > grid[row][col]:
                        grid[row - 1][col] = grid[row][col] + 1
                        dq.append((row - 1, col))
                    seen.add((row - 1, col))
                if row < len(grid) - 1 and grid[row + 1][col] != 0 and grid[row + 1][col] != 2 and grid[row + 1][col] not in seen:
                    if grid[row + 1][col] == 1 or grid[row + 1][col] > grid[row][col]:
                        grid[row + 1][col] = grid[row][col] + 1
                        dq.append((row + 1, col))
                    seen.add((row + 1, col))
                if col > 0 and grid[row][col - 1] != 0 and grid[row][col - 1] != 2 and grid[row][col - 1] not in seen:
                    if grid[row][col - 1] == 1 or grid[row][col - 1] > grid[row][col]:
                        grid[row][col - 1] = grid[row][col] + 1
                        dq.append((row , col - 1))
                    seen.add((row, col - 1))
                if col < len(grid[0]) - 1 and grid[row][col + 1] != 0 and grid[row][col + 1] != 2 and grid[row][col + 1] not in seen:
                    if grid[row][col + 1] == 1 or grid[row][col + 1] > grid[row][col]:
                        grid[row][col + 1] = grid[row][col] + 1
                        dq.append((row , col + 1))
                    seen.add((row, col + 1))

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 2:
                    bfs(m, n)

        result = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    return -1
                result = max(result, grid[m][n])
        return result - 2 if result != 0 else 0
