class Solution:
    def isValid(self, s: str) -> bool:
        ldic: dict[str, str] = {"{": "}", "(": ")", "[": "]"}
        rset: set[str] = {"}", ")", "]"}

        stack = []
        for c in s:
            if c in rset:
                if len(stack) == 0:
                    return False
                if ldic[stack[-1]] != c :
                    return False
                else:
                    stack.pop()
            elif c in ldic:
                stack.append(c)
            else:
                return False
        return True if len(stack) == 0 else False
