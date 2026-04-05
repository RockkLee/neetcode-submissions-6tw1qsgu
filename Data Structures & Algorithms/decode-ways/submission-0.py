from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        @lru_cache(None)
        def topdown(idx: int) -> int:
            # If we've consumed the entire string, that's one valid decoding.
            if idx == len(s):
                return 1

            # If current char is '0', it can't start a valid encoding.
            if s[idx] == "0":
                return 0

            # Option 1: use one digit
            ways = topdown(idx + 1)

            # Option 2: use two digits, if valid (10–26)
            if idx + 1 < len(s):
                two_digit = int(s[idx:idx + 2])
                if 10 <= two_digit <= 26:
                    ways += topdown(idx + 2)

            return ways

        return topdown(0)