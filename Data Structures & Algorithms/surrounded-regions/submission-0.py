class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_not_closed(row: int, col: int) -> bool:
            # only `O` elements would get iterated, so the region is not enclosed if a `O` is on the edge
            if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1:
                return True
            return False

        def bfs(r: int, c: int):
            seen: set[Tuple[int, int]] = {(r, c)}
            dq: deque[Tuple[int, int]] = deque()
            dq.append((r, c))
            while dq:
                row, col = dq.popleft()
                if is_not_closed(row, col):
                    return
                if row > 0 and (row - 1, col) not in seen:
                    if board[row - 1][col] == "O":
                        if is_not_closed(row - 1, col): return
                        dq.append((row - 1, col)); seen.add((row - 1, col))
                if row < len(board) - 1 and (row + 1, col) not in seen:
                    if board[row + 1][col] == "O":
                        if is_not_closed(row + 1, col): return
                        dq.append((row + 1, col)); seen.add((row + 1, col))
                if col > 0 and (row, col - 1) not in seen:
                    if board[row][col - 1] == "O":
                        if is_not_closed(row, col - 1): return
                        dq.append((row, col - 1)); seen.add((row, col - 1))
                if col < len(board[0]) - 1 and (row, col + 1) not in seen:
                    if board[row][col + 1] == "O":
                        if is_not_closed(row, col + 1): return
                        dq.append((row, col + 1)); seen.add((row, col + 1))
            for (row, col) in seen:
                board[row][col] = "X"

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    bfs(row, col)
