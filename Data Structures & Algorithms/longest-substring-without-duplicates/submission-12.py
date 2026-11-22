class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sett = set()
        maxx = 0
        for c in s:
            while c in sett:
                sett.remove(s[l])
                l += 1
            sett.add(c)
            maxx = max(maxx, len(sett))
        return maxx
