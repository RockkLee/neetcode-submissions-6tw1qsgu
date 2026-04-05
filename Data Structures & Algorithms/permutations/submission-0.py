class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol: List[int] = []
        res: List[List[int]] = []

        def backtracking(options: List[int]):
            # base case
            if not options:
                res.append(sol[:])
                return

            # make decisions
            for _, n in enumerate(options):
                sol.append(n)
                backtracking(list(filter(lambda ele: ele != n, options)))
                sol.pop() # undo the decision
        
        backtracking(nums)
        return res