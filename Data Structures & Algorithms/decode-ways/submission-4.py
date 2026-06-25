from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def topdown(i: int) -> int:
            if i >= n:
                return 1 if i == n else 0
            if s[i] == "0":
                return 0
            cnt = 0
            if i < n - 1 and 10 <= int(s[i:i+2]) <= 26:
                cnt += topdown(i + 2) 
            cnt += topdown(i + 1) if 0 <= int(s[i]) <= 9 else 0
            return cnt
        
        return topdown(0)

