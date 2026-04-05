from collections import deque
from typing import List, Tuple, Set


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        if m == 1 and n == 1:
            return [[0, 0]]

        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            vis: Set[Tuple[int, int]] = set(starts)
            dq: deque[Tuple[int, int]] = deque(starts)
            while dq:
                row, col = dq.popleft()
                h = heights[row][col]
                if row > 0 and (row - 1, col) not in vis and heights[row - 1][col] >= h:
                    vis.add((row - 1, col)); dq.append((row - 1, col))
                if row < m - 1 and (row + 1, col) not in vis and heights[row + 1][col] >= h:
                    vis.add((row + 1, col)); dq.append((row + 1, col))
                if col > 0 and (row, col - 1) not in vis and heights[row][col - 1] >= h:
                    vis.add((row, col - 1)); dq.append((row, col - 1))
                if col < n - 1 and (row, col + 1) not in vis and heights[row][col + 1] >= h:
                    vis.add((row, col + 1)); dq.append((row, col + 1))
            return vis

        pac_starts = [(0, col) for col in range(n)] + [(row, 0) for row in range(m)]
        atl_starts = [(m - 1, col) for col in range(n)] + [(row, n - 1) for row in range(m)]

        pac_set = bfs(pac_starts)
        atl_set = bfs(atl_starts)

        # Intersection of coordinates reachable from both oceans
        return [[row, col] for (row, col) in pac_set & atl_set]