class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsets = [set() for _ in range(9)]
        colsets = [set() for _ in range(9)]
        boxsets = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                box_idx = 3 * (r // 3) + (c // 3)

                if (
                    val in rowsets[r] or
                    val in colsets[c] or
                    val in boxsets[box_idx]
                ):
                    return False

                rowsets[r].add(val)
                colsets[c].add(val)
                boxsets[box_idx].add(val)

        return True