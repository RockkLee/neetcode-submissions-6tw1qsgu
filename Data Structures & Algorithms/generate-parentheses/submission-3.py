import copy
from collections import deque
from typing import List


class Solution:
    """
    Given n pairs of parentheses,
    write a function to generate all combinations of well-formed parentheses.

    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:
    Input: n = 1
    Output: ["()"]
    """

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []

        def backtracking(l_p_cnt: int, r_p_cnt: int):
            # Base case (To end the recursion)
            if l_p_cnt == n and r_p_cnt == n:
                res.append("".join(sol))
                return

            # Make decisions
            if l_p_cnt < n:
                sol.append("(")
                backtracking(l_p_cnt + 1, r_p_cnt)
                sol.pop() # Undo decision
            if r_p_cnt < n and r_p_cnt < l_p_cnt:
                sol.append(")")
                backtracking(l_p_cnt, r_p_cnt + 1)
                sol.pop() # Undo decision

        backtracking(0, 0)
        return res
