class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo: dict[tuple[int, int], bool] = {}

        def is_palindrome(l: int, r: int) -> bool:
            if (l, r) in memo:
                return memo[(l, r)]

            if l >= r:
                memo[(l, r)] = True
                return True

            memo[(l, r)] = s[l] == s[r] and is_palindrome(l + 1, r - 1)
            return memo[(l, r)]

        count = 0

        for l in range(n):
            for r in range(l, n):
                if is_palindrome(l, r):
                    count += 1

        return count