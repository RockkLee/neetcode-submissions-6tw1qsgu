def _is_palindrome(s: str, l: int, r: int) -> bool:
    while l <= r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res: List[List[str]] = []
        path: List[str] = []

        def backtracking(idx: int):
            if idx >= len(s):
                res.append(path[:])
                return
            for i in range(idx, len(s)):
                if _is_palindrome(s, idx, i):
                    path.append(s[idx:i + 1])
                    backtracking(i + 1)
                    path.pop()

        backtracking(0)
        return res
