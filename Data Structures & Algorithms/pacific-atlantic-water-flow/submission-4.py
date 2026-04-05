class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_deq: deque[Tuple[int, int]] = deque()
        p_visited: set[Tuple[int, int]] = set()
        a_deq: deque[Tuple[int, int]] = deque()
        a_visited: set[Tuple[int, int]] = set()
        rows, cols = len(heights), len(heights[0])

        for c in range(cols):
            p_deq.append((0, c))
            p_visited.add((0, c))
        for r in range(1, rows):
            p_deq.append((r, 0))
            p_visited.add((r, 0))
        for c in range(cols):
            a_deq.append((rows - 1, c))
            a_visited.add((rows - 1, c))
        for r in range(0, rows - 1):
            a_deq.append((r, cols - 1))
            a_visited.add((r, cols - 1))

        def bfs(dq: deque, visited: set):
            while dq:
                r, c = dq.popleft()
                for r_off, c_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    pos = (r + r_off, c + c_off)
                    if (0 <= pos[0] < rows and 0 <= pos[1] < cols and
                            pos not in visited and heights[pos[0]][pos[1]] >= heights[r][c]):
                        dq.append(pos)
                        visited.add(pos)

        bfs(p_deq, p_visited)
        bfs(a_deq, a_visited)

        return list(p_visited.intersection(a_visited))
