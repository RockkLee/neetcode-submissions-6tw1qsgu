from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @lru_cache(maxsize=None)
        def topdown(idx: int):
            if idx == len(s):
                return True
            # check if any substrings are in word_set starting from current char to the last letter
            for r in range(idx + 1, len(s) + 1):
                # if s[idx:r] in word_set -> idx move to the next char after the matched word
                if s[idx:r] in word_set and topdown(r):
                    return True
            return False
        return topdown(0)
