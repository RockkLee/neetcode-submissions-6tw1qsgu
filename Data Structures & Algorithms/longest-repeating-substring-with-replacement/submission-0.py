class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        if length == 1:
            return 1
        l = 0
        maxx = 0
        dic = {}
        for r, ch in enumerate(s):
            dic[ch] = dic.get(ch, 0) + 1
            # shrink the window if its length (max num of same chars) is larger than k
            max_freq = max(dic.values())
            while r - l + 1 - max_freq > k:
                dic[s[l]] -= 1
                l += 1
            maxx = max(r - l + 1, maxx) # freq = len(window)
        return maxx
