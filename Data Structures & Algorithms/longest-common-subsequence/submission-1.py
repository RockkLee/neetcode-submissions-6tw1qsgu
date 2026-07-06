from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def topdown(i: int, j:int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            cnt = 0
            # always take it 
            if text1[i] == text2[j]:
                return topdown(i + 1, j + 1) + 1
            # choose which char should be checked next
            return max(topdown(i + 1, j), topdown(i, j + 1))
        return topdown(0, 0)