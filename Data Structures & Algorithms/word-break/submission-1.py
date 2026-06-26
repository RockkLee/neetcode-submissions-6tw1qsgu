from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sett = set(wordDict)
        n = len(s)

        @cache
        def topdown(i: int) -> bool:
            if i == n:
                return True

            for r in range(i + 1, n + 1):
                if s[i:r] in sett and topdown(r):
                    return True

            return False

        return topdown(0)