# 7, 1, 7, 2, 2, 4
#    i
# 1 - 0 * 7
# stack: [(7, 0), 1]

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: list[tuple[int, int]] = [] # height, idx
        maxx = 0
        for idx in range(len(heights)):
            pos = idx
            while stack and stack[-1][0] > heights[idx]:
                h, i = stack.pop()
                maxx = max(maxx, (idx - i) * h)
                pos = i
            stack.append((heights[idx], pos))
        while stack:
            h, pos = stack.pop()
            maxx = max(maxx, h * (len(heights) - pos))
        return maxx
