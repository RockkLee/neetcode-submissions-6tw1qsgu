from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dic = defaultdict(int)
        max_freq = 0
        max_len = 0

        for r in range(len(s)):
            dic[s[r]] += 1
            max_freq = max(max_freq, dic[s[r]])

            if (r - l + 1) - max_freq > k:
                dic[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len