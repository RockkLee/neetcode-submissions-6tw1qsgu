from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)
        for k in s_dict.keys():
            if s_dict[k] != t_dict[k]:
                return False
        return True
