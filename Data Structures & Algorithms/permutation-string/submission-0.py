class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dic, comparison_dic = {}, {}
        for idx, _ in enumerate(s1):
            comparison_dic[s1[idx]] = comparison_dic.get(s1[idx], 0) + 1
            dic[s2[idx]] = dic.get(s2[idx], 0) + 1
        if dic == comparison_dic:
            return True

        dic[s2[0]] -= 1
        if dic[s2[0]] == 0:
            dic.pop(s2[0])
        l = 1
        for r in range(len(s1), len(s2)):
            dic[s2[r]] = dic.get(s2[r], 0) + 1
            if dic == comparison_dic:
                return True
            dic[s2[l]] -= 1
            if dic[s2[l]] == 0:
                dic.pop(s2[l])
            l += 1

        if dic == comparison_dic:
            return True
        else:
            return False
