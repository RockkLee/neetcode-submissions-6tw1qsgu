class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []
        path: List[str] = []

        def backtracking(lcnt: int, rcnt: int):
            if lcnt > n or rcnt > n:
                return
            if lcnt == n and rcnt == n:
                res.append("".join(path))
                return
            path.append("(")
            backtracking(lcnt + 1, rcnt)
            path.pop()
            if lcnt > rcnt:
                path.append(")")
                backtracking(lcnt, rcnt + 1)
                path.pop()

        backtracking(0, 0)
        return res
