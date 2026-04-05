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
        tmp_res = deque()
        sol = []

        def backtracking(l_p_cnt: int, r_p_cnt: int):
            if l_p_cnt == n and r_p_cnt == n:
                tmp_res.append(copy.deepcopy(sol))
                return

            if l_p_cnt < n and (sol not in tmp_res):
                sol.append("(")
                backtracking(l_p_cnt + 1, r_p_cnt)
                sol.pop()
            if r_p_cnt < n and r_p_cnt < l_p_cnt and (sol not in tmp_res):
                sol.append(")")
                backtracking(l_p_cnt, r_p_cnt + 1)
                sol.pop()

        backtracking(0, 0)

        res = [None] * len(tmp_res)
        for i, ls in enumerate(tmp_res):
            res[i] = "".join(ls)

        return res
