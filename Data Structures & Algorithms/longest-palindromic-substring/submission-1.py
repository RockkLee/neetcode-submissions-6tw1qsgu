from functools import cache

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        @cache
        def is_palindrome(l: int, r: int) -> bool:
            if l >= r:
                return True
            return s[l] == s[r] and is_palindrome(l + 1, r - 1)

        best_l, best_r = 0, 0

        for l in range(n):
            for r in range(l, n):
                if is_palindrome(l, r) and r - l > best_r - best_l:
                    best_l, best_r = l, r

        return s[best_l:best_r + 1]

            
                
        
