class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        sett = set()
        l = 0
        maxx = 0
        for r in range(len(s)):
            if s[r] in sett:
                while s[l] != s[r]:
                    sett.remove(s[l])
                    l += 1
                l += 1
            else:
                sett.add(s[r])
            maxx = max(r - l + 1, maxx)
        return maxx
