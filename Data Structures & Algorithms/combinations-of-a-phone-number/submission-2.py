class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        path: List[str] = []
        res: List[str] = []

        def backtracking(idx: int):
            nonlocal path
            # base case
            if idx == len(digits):
                res.append("".join(path))
                return

            # make decisions
            letters = dic[digits[idx]]
            for _, letter in enumerate(letters):
                path.append(letter)
                backtracking(idx + 1)
                path.pop()

        backtracking(0)
        return res
