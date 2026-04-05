class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxx = 0
        while l < r:
            maxx = max(min(height[l], height[r]) * (r - l), maxx)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxx
