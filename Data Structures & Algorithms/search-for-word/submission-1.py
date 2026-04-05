from typing import List, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        chk = False
        path: list[Tuple[int, int]] = []  # List[Tuple[m, n]]

        def backtracking(seen: set[Tuple[int, int]], pos: Tuple[int, int]):
            nonlocal chk
            if chk:  # early exit if already found
                return

            pos_m = pos[0]
            pos_n = pos[1]

            # (your corner/blocked checks left as-is; they are harmless but unnecessary)

            seen.add((pos_m, pos_n))
            # make decisions
            path.append((pos_m, pos_n))  # take it

            # ---- CHANGES: prune by prefix and check completion ----
            # If current letter doesn't match the corresponding char in word, backtrack
            if len(path) > len(word) or board[pos_m][pos_n] != word[len(path) - 1]:
                path.pop()
                return

            # If we've matched the whole word, success
            if len(path) == len(word):
                chk = True
                return
            # --------------------------------------------------------

            if pos_m != 0 and (pos_m - 1, pos_n) not in seen:
                backtracking(seen.copy(), (pos_m - 1, pos_n))
            if pos_m != len(board) - 1 and (pos_m + 1, pos_n) not in seen:
                backtracking(seen.copy(), (pos_m + 1, pos_n))
            if pos_n != 0 and (pos_m, pos_n - 1) not in seen:
                backtracking(seen.copy(), (pos_m, pos_n - 1))
            if pos_n != len(board[0]) - 1 and (pos_m, pos_n + 1) not in seen:
                backtracking(seen.copy(), (pos_m, pos_n + 1))

            path.pop()  # undo the decision

            # ---- CHANGES: stop here; "not take it" doesn't apply to this problem ----
            return
            # (your original "not take it" neighbor calls remain below but are unreachable)
            # --------------------------------------------------------------------------

        # ---- CHANGES: try every starting cell (not just (0,0)) ----
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    path.clear()
                    backtracking(set(), (i, j))
                    if chk:
                        return True
        return False
