from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dic = defaultdict(int)
        maxx = 0

        for r in range(len(s)):
            dic[s[r]] += 1
            while (r - l + 1) - max(dic.values()) > k:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
            maxx = max(maxx, r - l + 1)
        return maxx