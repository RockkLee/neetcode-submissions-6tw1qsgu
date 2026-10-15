class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = 0
            if heights[l] < heights[r]:
                height = heights[l]
                l += 1
            else:
                height = heights[r]
                r -= 1
            maxx = max(maxx, height * width)
        return maxx