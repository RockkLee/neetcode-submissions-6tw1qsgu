class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sett = set()
        maxx = 0
        for i, c in enumerate(s):
            while c in sett:
                sett.remove(s[l])
                l += 1
            sett.add(c)
            maxx = max(maxx, len(sett))
        return maxx
