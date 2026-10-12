# leetcode 125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            left, right = s[l], s[r]

            if not left.isalnum():
                l += 1
                continue

            if not right.isalnum():
                r -= 1
                continue

            if left.lower() != right.lower():
                return False

            l += 1
            r -= 1

        return True