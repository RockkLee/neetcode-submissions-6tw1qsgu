from functools import lru_cache


class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache(None)
        def backtracking(i:int, left: int) -> bool:
            if left < 0:  # prevent from ")", "())"
                return False
            if i == len(s):
                if left != 0:
                    return False
                return True
            if s[i] == "(":
                if backtracking(i + 1, left + 1):
                    return True
            elif s[i] == ")":
                if backtracking(i + 1, left - 1):
                    return True
            else:  # s[i] = *
                if backtracking(i + 1, left + 1):
                    return True
                if backtracking(i + 1, left):
                    return True
                if backtracking(i + 1, left - 1):
                    return True
            return False
        return backtracking(0, 0)
