class Solution:
    def partition(self, wrd: str) -> List[List[str]]:
        res: set[Tuple] = set()
        sol: List[str] = [wrd[0]]
        wrd = wrd[1:]

        def backtracking(idx: int):
            # base case
            if idx == len(wrd):
                for s in sol:
                    if s != s[::-1]: return
                res.add(tuple(sol))
                return

            # make decisions
            # take it
            s = sol[-1] + wrd[idx]
            sol[-1] = s
            backtracking(idx + 1)
            sol[-1] = s[:len(s) - 1]  # undo the decision
            # not take it
            sol.append(wrd[idx])
            backtracking(idx + 1)
            sol.pop()  # undo the decision

        backtracking(0)
        return [list(tup) for tup in res]